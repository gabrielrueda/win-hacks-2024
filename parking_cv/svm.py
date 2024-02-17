from sklearn.model_selection import GridSearchCV
import numpy as np
import cv2  
import imutils
from imutils import perspective 
from imutils.video import count_frames
import numpy as np
from matplotlib import pyplot as plt 
import time

from tools import image_utils
from sklearn.svm import SVC
# from sklearn.externals import joblib
import pickle as pkl


class SVM ():
    
    def __init__(self):
        self.svm = SVC(C = 0.001, kernel='linear', verbose = True)
    
    def train(self, X_train, y_train, X_test, y_test):
        from sklearn.model_selection import cross_val_score


        cv_performance = cross_val_score(self.svm, X_train, y_train, cv=20)

        test_performance = self.svm.fit(X_train, y_train).score(X_test, y_test)

        print ('Cross-validation accuracy score: %0.3f, test accuracy score: %0.3f'% (np.mean(cv_performance),test_performance))

        self.save(self.svm, True)





    def search_parameter(self, X_train, y_train, X_test, y_test):

        learning_algo = SVC(kernel='linear', random_state=101)
        search_space = [{'kernel': ['linear'],'C': np.logspace(-3, 3, 7)}, {'kernel': ['rbf'],'C':np.logspace(-3, 3, 7),'gamma': np.logspace(-3, 2, 6)}]
        gridsearch = GridSearchCV(learning_algo, param_grid=search_space,refit=True, cv=10)

        gridsearch.fit(X_train,y_train)

        print ('Best parameter: %s'% str(gridsearch.best_params_))

        cv_performance = gridsearch.best_score_

        test_performance = gridsearch.score(X_test, y_test)

        print ('Cross-validation accuracy score: %0.3f, test accuracy score: %0.3f' % (cv_performance,test_performance))


    def save(self, model, check, filename = 'finalized_model.pkl'):

        if check != True:
            anw = input("Você quer Salvar o modelo? y/n")
        else:
            anw = 'y'

        if anw == 'y' :
            with open(filename, 'wb') as f:
                pkl.dump(model, f)
            print("Saved")
        else:
            print("No Saved")
   

    def test(self, X_test, Y_test, filename = 'finalized_model.pkl'):
        # load the model from disk
        with open(filename, 'rb') as f:
            loaded_model = pkl.load(f)
            result = loaded_model.score(X_test, Y_test)
            print(result)

    def predict (self, test, filename = 'finalized_model.pkl'):
        with open(filename, 'rb') as f:
            model = pkl.load(f)
            list_temp = []
            for i in test:
                i = i.reshape((1,len(i)))
                pred = model.predict(i)
                print(pred)
                list_temp.append(pred)
            
            return list_temp




class Call_SVM():

    def load_prepare_data(self, empty_path = 'dataset/rawdataset/empty', occupied_path = 'dataset/rawdataset/occupied'):
        
        empty = image_utils().load_image_from_path(empty_path)
        occup = image_utils().load_image_from_path(occupied_path)

        #print(empty)

        train_empty = empty[0:100]
        test_empty = empty[100:150]

        train_occup = occup[0:100]
        test_occup = occup[100:150]

        train_empty = np.asarray(train_empty)
        #print(train_empty.shape)
        base_train = np.concatenate([train_empty, train_occup])
        base_test = np.concatenate([test_empty, test_occup])

        #print(base_train.shape)
        #print(base_test.shape)


        labels_train = np.zeros(200, dtype=np.int64)
        labels_train[100:200] = np.ones(100, dtype=np.int64)

        labels_test = np.zeros(100, dtype=np.int64)
        labels_test[50:100] = np.ones(50, dtype=np.int64)

        #print(labels_train[0:100])


        train_zip = zip (base_train,labels_train)
        test_zip = zip (base_test,labels_test)
        
        return base_train,base_test, labels_train, labels_test
        #return train_zip,test_zip

    


    def training(self):

        base_train,base_test, labels_train, labels_test = self.load_prepare_data()

        features_train = image_utils().extract_features(base_train)
        features_test = image_utils().extract_features(base_test)


        SVM().train(features_train,labels_train,features_test,labels_test)
        #SVM().test(features_test,labels_test)

        features_test = features_test[94].reshape(1,-1)
        SVM().predict(features_test)


    def testing (self):
        base_train,base_test, labels_train, labels_test = self.load_prepare_data()

        features_train = image_utils().extract_features(base_train)
        features_test = image_utils().extract_features(base_test)


        SVM().test(features_test,labels_test)

        







        

#Call_SVM().training()
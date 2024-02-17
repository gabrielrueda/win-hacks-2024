import cv2  
import imutils
from imutils import perspective 
from imutils.video import count_frames
import numpy as np
from matplotlib import pyplot as plt 
import time
from tools import image_utils
from svm import SVM, Call_SVM
import datetime


path = 'test4.mp4'
vs = cv2.VideoCapture(path)
fps = 12
capSize = (640,360)
#capSize = (1920,1080)
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter()
success = out.open('./test5.mp4',fourcc,fps,capSize,True)

num_frames = count_frames(path)
print(num_frames)

Call_SVM().training()
print("Trained")

# get_point = 0  
i = 0 

while i < num_frames:
    ret, frame = vs.read()
    frame = imutils.resize(frame, width=450)  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gau = cv2.GaussianBlur(gray, (7, 7), 0)

    
    # Not work yet

    # if get_point == True:
    #     number_of_places = 2 # Defini o numero de vagas que voce ira selecionar 
    #     boxes = image_utils.getSpotsCoordiantesFromImage(frame, number_of_places)
    #     boxes = asarray(boxes)
    #     print(boxes)
    #     check = False

    # else:
    box1 = np.array ([(108, 410), (72, 273), (72, 273), (72, 273)])
    box2 = np.array ([(200, 420), (133, 280), (133, 280), (133, 280)])
    box3 = np.array ([(300, 434), (200, 289), (200, 289), (200, 289)])
    box4 = np.array ([(406, 434), (270, 289), (270, 289), (270, 289)])
    box5 = np.array ([(522, 438), (348, 292), (348, 292), (348, 292)])
    box6 = np.array ([(646, 444), (430, 296), (430, 296), (430, 296)])
    box7 = np.array ([(762, 448), (508, 298), (508, 298), (508, 298)])
    box8 = np.array ([(868, 452), (578, 301), (578, 301), (578, 301)])
    box9 = np.array ([(962, 448), (641, 298), (641, 298), (641, 298)])
    box10 = np.array ([(1052, 450), (701, 300), (701, 300), (701, 300)])
    box11 = np.array ([(1128, 444), (752, 296), (752, 296), (752, 296)])

    boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11]
    img_resize = image_utils.getRotateRect(gau, boxes)
    feature = image_utils().extract_features(img_resize)

    '''feature1 = feature.reshape(-1, 1)
    score0 = SVM().predict(feature1)
    score1 = SVM().predict(feature[1])

    print (score0, score1)'''


    timestamp = datetime.datetime.now()
    score = SVM().predict(feature)

    car_exit = False

    if score[0] == 0: 
        cv2.polylines(frame,np.int32([box1]), True ,(0,0,255),2  )
        car_exit = False
        i = 0
    else:
        cv2.polylines(frame,np.int32([box1]),True,(0,255,0), 2)

        if car_exit == False:
            cv2.putText(frame, timestamp.strftime(" car_exit as: %d %m %Y %I:%M:%S"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0),2)
            i += 1
            if i > 100: 
                car_exit = True

    if score[1] == 0: 
        cv2.polylines(frame,np.int32([box2]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box2]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)



    

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # If the 'q' key is pressed, the loop ends
    if key == ord("q"):
        break

    if key == ord('p'):
        hist = cv2.calcHist([a[1]], [0], None, [256], [0,256])
        plt.plot(hist)
        plt.show()


    i += 1 









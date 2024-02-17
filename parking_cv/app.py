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
    box1 = np.array ([(37, 124), (8, 25), (8, 25), (8, 25)])
    box2 = np.array ([(69, 127), (15, 25), (15, 25), (15, 25)])
    box3 = np.array ([(104, 132), (24, 26), (24, 26), (24, 26)])
    box4 = np.array ([(141, 132), (32, 26), (32, 26), (32, 26)])
    box5 = np.array ([(181, 133), (41, 26), (41, 26), (41, 26)])
    box6 = np.array ([(224, 135), (51, 27), (51, 27), (51, 27)])
    box7 = np.array ([(264, 136), (61, 27), (61, 27), (61, 27)])
    box8 = np.array ([(301, 137), (69, 27), (69, 27), (69, 27)])
    box9 = np.array ([(334, 136), (77, 27), (77, 27), (77, 27)])
    box10 = np.array ([(365, 137), (84, 27), (84, 27), (84, 27)])
    box11 = np.array ([(392, 135), (90, 27), (90, 27), (90, 27)])

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









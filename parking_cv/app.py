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
    box1 = np.array ([(54, 205), (26, 203), (0, 240), (25, 256)])
    box2 = np.array ([(100, 210), (62, 207), (30, 258), (69, 263)])
    box3 = np.array ([(150, 217), (109, 211), (77, 265), (120, 271)])
    box4 = np.array ([(203, 217), (160, 214), (130, 273), (184, 280)])
    box5 = np.array ([(261, 219), (213, 217), (195, 279), (256, 283)])
    box6 = np.array ([(323, 222), (273, 220), (268, 280), (325, 282)])
    box7 = np.array ([(381, 224), (335, 222), (336, 286), (390, 287)])
    box8 = np.array ([(434, 226), (392, 224), (402, 286), (458, 286)])
    box9 = np.array ([(481, 224), (443, 225), (467, 284), (515, 287)])
    box10 = np.array ([(526, 225), (492, 226), (522, 285), (560, 279)])
    box11 = np.array ([(564, 222), (533, 225), (565, 277), (599, 272)])

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


    if score[2] == 0: 
        cv2.polylines(frame,np.int32([box3]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box3]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)


    if score[3] == 0: 
        cv2.polylines(frame,np.int32([box4]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box4]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)


    if score[4] == 0: 
        cv2.polylines(frame,np.int32([box5]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box5]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)


    if score[5] == 0: 
        cv2.polylines(frame,np.int32([box6]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box6]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)


    if score[6] == 0: 
        cv2.polylines(frame,np.int32([box7]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box7]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)


    if score[7] == 0: 
        cv2.polylines(frame,np.int32([box8]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box8]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)


    if score[8] == 0: 
        cv2.polylines(frame,np.int32([box9]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box9]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)


    if score[9] == 0: 
        cv2.polylines(frame,np.int32([box10]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box10]),True,(0,255,0), 2)
        cv2.putText(frame, timestamp.strftime(" %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.35, (0, 0, 255), 5)

    if score[10] == 0: 
        cv2.polylines(frame,np.int32([box11]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box11]),True,(0,255,0), 2)
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









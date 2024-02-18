import mysql.connector
import cv2  
import imutils
from imutils import perspective 
from imutils.video import count_frames
import numpy as np
from matplotlib import pyplot as plt 
import time
from tools import image_utils
from svm import SVM, Call_SVM
from datetime import datetime, date, timedelta


#where i am storing database authorization credentials
credentials = []

#import credentials from a text file
with open('credentials.txt', 'r') as f:
    for content in f:
        #add to array of content
        credentials.append(content.strip())

#db credentials for database\
conn = mysql.connector.connect(
    host=credentials[0],
    user=credentials[1],
    password=credentials[2],
    database=credentials[3]
)

# Create a cursor object
cursor = conn.cursor()



# path = './videos/sample_vid.mp4'
# vs = cv2.VideoCapture(path)

vs = cv2.VideoCapture(0)
fps = 12
capSize = (640,360)
#capSize = (1920,1080)
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter()
success = out.open('./videos/output.mp4',fourcc,fps,capSize,True)

# num_frames = count_frames(path)
# print(num_frames)

Call_SVM().training()
print("Trained")

past_time = time.time()

while True:
    ret, tmp_frame = vs.read()
    tmp_frame = imutils.resize(tmp_frame, width=450)

    # tmp_frame_2 = cv2.convertScaleAbs(tmp_frame, alpha=0.8, beta=0.0); 

    # # alpha: brightness
    # # beta: contrast
    
    # frame = cv2.cvtColor(tmp_frame_2, cv2.COLOR_BGR2HSV)
    # # Adjust the hue, saturation, and value of the image 
    # # Adjusts the hue by multiplying it by 0.7 
    # frame[:, :, 0] = frame[:, :, 0] * 1.0
    # # Adjusts the saturation by multiplying it by 1.5 
    # frame[:, :, 1] = frame[:, :, 1] * 1.0
    # # Adjusts the value by multiplying it by 0.5 
    # frame[:, :, 2] = frame[:, :, 2] * 1.0


    # (h,s,v) = cv2.split(frame)
    # v[:] = 100
    # img = cv2.merge((v, v, s))

    # # frame = tmp_frame
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)	


    frame = tmp_frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = tmp_frame
    gau = cv2.GaussianBlur(gray, (7, 7), 0)

    box1 = np.array ([(42, 142), (13, 142), (0, 159), (20, 173)])
    box2 = np.array ([(77, 142), (49, 143), (30, 176), (60, 180)])
    box3 = np.array ([(121, 142), (82, 143), (70, 178), (105, 181)])
    box4 = np.array ([(165, 146), (127, 145), (118, 183), (155, 185)])
    box5 = np.array ([(218, 146), (175, 145), (168, 182), (222, 180)])
    box6 = np.array ([(269, 148), (227, 146), (227, 184), (275, 186)])
    box7 = np.array ([(310, 149), (275, 147), (285, 186), (322, 185)])
    box8 = np.array ([(352, 150), (319, 149), (334, 188), (368, 186)])
    box9 = np.array ([(351, 158), (325, 159), (342, 201), (376, 203)])
    box10 = np.array ([(384, 159), (360, 160), (381, 201), (408, 197)])
    box11 = np.array ([(411, 157), (388, 159), (411, 196), (435, 192)])

    boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11]
    img_resize = image_utils.getRotateRect(gau, boxes)
    feature = image_utils().extract_features(img_resize)


    # timestamp = datetime.datetime.now()
    score = SVM().predict(feature)

    # result is the list of 1's and 0's that can be sent to the leds
    result = []

    for x in score:
        result.append(x[0])

    curr_time = time.time()
    if(curr_time - past_time > 2):
        print("update db")
        past_time = curr_time
        insert_query = "INSERT INTO PARKING_SLOTS VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Execute the query with the Python variables as parameters

        cursor.execute(insert_query, (datetime.now(), True if result[0] == 1 else False, True if result[1] == 1 else False, True if result[2] == 1 else False, True if result[3] == 1 else False, True if result[4] == 1 else False, True if result[5] == 1 else False, True if result[6] == 1 else False, True if result[7] == 1 else False, True if result[8] == 1 else False, True if result[9] == 1 else False, True if result[10] == 1 else False))
        conn.commit()


    car_exit = False 

    if score[0] == 0: 
        cv2.polylines(frame,np.int32([box1]), True ,(0,0,255),2 )
    else:
        cv2.polylines(frame,np.int32([box1]),True,(0,255,0), 2)

    if score[1] == 0: 
        cv2.polylines(frame,np.int32([box2]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box2]),True,(0,255,0), 2)

    if score[2] == 0: 
        cv2.polylines(frame,np.int32([box3]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box3]),True,(0,255,0), 2)

    if score[3] == 0: 
        cv2.polylines(frame,np.int32([box4]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box4]),True,(0,255,0), 2)

    if score[4] == 0: 
        cv2.polylines(frame,np.int32([box5]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box5]),True,(0,255,0), 2)

    if score[5] == 0: 
        cv2.polylines(frame,np.int32([box6]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box6]),True,(0,255,0), 2)
        
    if score[6] == 0: 
        cv2.polylines(frame,np.int32([box7]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box7]),True,(0,255,0), 2)

    if score[7] == 0: 
        cv2.polylines(frame,np.int32([box8]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box8]),True,(0,255,0), 2)
 
    if score[8] == 0: 
        cv2.polylines(frame,np.int32([box9]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box9]),True,(0,255,0), 2)

    if score[9] == 0: 
        cv2.polylines(frame,np.int32([box10]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box10]),True,(0,255,0), 2)
        
    if score[10] == 0: 
        cv2.polylines(frame,np.int32([box11]), True ,(0,0,255),2  )
    else:
        cv2.polylines(frame,np.int32([box11]),True,(0,255,0), 2)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    # If the 'q' key is pressed, the loop ends
    # if key == ord("q"):
    #     break

    # if key == ord('p'):
    #     hist = cv2.calcHist([a[1]], [0], None, [256], [0,256])
    #     plt.plot(hist)
    #     plt.show()


cursor.close()
conn.close()

cv2.destroyAllWindows()

vs.release() 
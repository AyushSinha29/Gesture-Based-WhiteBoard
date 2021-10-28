import numpy as np
import cv2
from collections import deque
import mediapipe as mp
import math

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

Drag = False
DragLeave = True

def setValues(x):
   print("")

cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180,setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180,setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255,setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 49, 255,setValues)

bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]

blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

kernel = np.ones((5,5),np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

paintWindow = np.zeros((480,640,3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40,1), (140,30), (1,1,1), 2)
paintWindow = cv2.rectangle(paintWindow, (140,1), (240,30), colors[0], -1)
paintWindow = cv2.rectangle(paintWindow, (240,1), (340,30), colors[1], -1)
paintWindow = cv2.rectangle(paintWindow, (340,1), (440,30), colors[2], -1)
paintWindow = cv2.rectangle(paintWindow, (440,1), (540,30), colors[3], -1)

cv2.putText(paintWindow, "Available colors: ", (8, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)


paintWindow = cv2.line(paintWindow, (0,480), (640,480), (0, 255, 0), 2)
  
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    Flipped = cv2.flip(frame, 1)
    results = hands.process(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)
                h, w, c = frame.shape

                # Check Hovering
                HoverDist = math.sqrt(((hand.landmark[8].x - hand.landmark[5].x) * w) ** 2 + (
                        (hand.landmark[8].y - hand.landmark[5].y) * h) ** 2)
                if HoverDist > 30:
                    frame = cv2.putText(frame, "Locating palm at (" + str(int(hand.landmark[8].x*w)) + ", " + str(int(hand.landmark[8].y*h)) + ")",
                                        (20, 50), cv2.FONT_HERSHEY_PLAIN, 1, 2)


               # Change to green color
                Change2G = math.sqrt(((hand.landmark[5].x - hand.landmark[4].x) * w) ** 2 + (
                        (hand.landmark[5].y - hand.landmark[4].y) * h) ** 2)

                if Change2G <10:
                    frame = cv2.putText(frame, "GREEN COLOR",
                                        (20, 70), cv2.FONT_HERSHEY_PLAIN, 1, 2)     
                
                    colorIndex = 1  

                # Change to red color
                Change2R = math.sqrt(((hand.landmark[17].x - hand.landmark[4].x) * w) ** 2 + (
                         (hand.landmark[17].y - hand.landmark[4].y) * h) ** 2)

                if Change2R <35:
                     frame = cv2.putText(frame, "RED COLOR",
                                         (20, 70), cv2.FONT_HERSHEY_PLAIN, 1, 2)     
                
                     colorIndex = 2 

                # Change to yellow color
                Change2Y = math.sqrt(((hand.landmark[8].x - hand.landmark[7].x) * w) ** 2 + (
                         (hand.landmark[8].y - hand.landmark[7].y) * h) ** 2)

                if Change2Y <10:
                     frame = cv2.putText(frame, "YELLOW COLOR",
                                         (20, 70), cv2.FONT_HERSHEY_PLAIN, 1, 2)     
                
                     colorIndex = 3 

                # Change back to blue color    
                Blue_1 = math.sqrt(((hand.landmark[5].x - hand.landmark[7].x) * w) ** 2 + (
                        (hand.landmark[5].y - hand.landmark[7].y) * h) ** 2)
                Blue_2 = math.sqrt(((hand.landmark[9].x - hand.landmark[11].x) * w) ** 2 + (
                        (hand.landmark[9].y - hand.landmark[11].y) * h) ** 2)
                Blue_3 = math.sqrt(((hand.landmark[13].x - hand.landmark[15].x) * w) ** 2 + (
                        (hand.landmark[13].y - hand.landmark[15].y) * h) ** 2)
                Blue_4 = math.sqrt(((hand.landmark[17].x - hand.landmark[19].x) * w) ** 2 + (
                        (hand.landmark[17].y - hand.landmark[19].y) * h) ** 2)
                Blue_5 = math.sqrt(((hand.landmark[5].x - hand.landmark[6].x) * w) ** 2 + (
                        (hand.landmark[5].y - hand.landmark[6].y) * h) ** 2)
                Blue_6 = math.sqrt(((hand.landmark[9].x - hand.landmark[10].x) * w) ** 2 + (
                        (hand.landmark[9].y - hand.landmark[10].y) * h) ** 2)
                Blue_7 = math.sqrt(((hand.landmark[13].x - hand.landmark[14].x) * w) ** 2 + (
                        (hand.landmark[13].y - hand.landmark[14].y) * h) ** 2)
                Blue_8 = math.sqrt(((hand.landmark[17].x - hand.landmark[18].x) * w) ** 2 + (
                        (hand.landmark[17].y - hand.landmark[18].y) * h) ** 2)


                if (Blue_1 < 25 and Blue_2<25 and Blue_3<25 and Blue_4<25) or \
                        (Blue_5 < 25 and Blue_6<25 and Blue_7<25 and Blue_8<25) :
                    frame = cv2.putText(frame, "BLUE COLOR " ,
                                        (20, 70), cv2.FONT_HERSHEY_PLAIN, 1, 2)
                    colorIndex = 0


    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
    Upper_hsv = np.array([u_hue,u_saturation,u_value])
    Lower_hsv = np.array([l_hue,l_saturation,l_value])
 
    cv2.putText(frame, "CLEAR", (50, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, " 'x' to quit", (500, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    Mask = cv2.erode(Mask, kernel, iterations=1)
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
    Mask = cv2.dilate(Mask, kernel, iterations=1)

    cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if len(cnts) > 0:
 
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
 
        if center[1] <= 65:
            if 40 <= center[0] <= 140: # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0

                paintWindow[60:,:,:] = 255
                
  
        else :
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)

    else:

        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1

    points = [bpoints, gpoints, rpoints, ypoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Canvas", paintWindow)


	# If the 'x' key is pressed then stop the application 
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break


cap.release()
cv2.destroyAllWindows()
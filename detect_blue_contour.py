import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):		
	_, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	res = cv2.bitwise_and(frame,frame, mask= mask)

    img_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    ret, im = cv2.threshold(img_gray, 100, 120, cv2.THRESH_BINARY_INV)
    contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt=contours[0]
    area=cv2.contourArea(cnt)
    img = cv2.drawContours(frame, contours, -1, (0,255,75), 2)
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
	    break
	

cv2.destroyAllWindows()
cap.release()

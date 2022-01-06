import cv2
import numpy as np

def show_image(image):
    small = cv2.resize(image, (0,0), fx=0.3, fy=0.3) 
    cv2.imshow('image',small)
    c = cv2.waitKey()
    if c >= 0 : return -1
    return 0


image = cv2.imread('/home/crossfire/Programming projects/AUV2k19/self-test/auv1.jpg')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, im = cv2.threshold(img_gray, 30, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[0]
print("\ncontours: ",contours)
area=cv2.contourArea(cnt)
img = cv2.drawContours(image, contours, -1, (0,255,75), 2)
print("\nContour area",area)
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cx, cy = (x + w/2), (y + h/2)
cv2.circle(overlay, (int(cx), int(cy)), 20, (0, 0, 255), -1)
draw_centroid(image, cx, cy)
print("\n\n\n",x,y,w,h)
show_image(img)


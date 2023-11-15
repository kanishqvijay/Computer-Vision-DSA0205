import cv2
import numpy as np
kernal = np.ones((5,5),np.uint8)
path = "car.jpeg"
img = cv2.imread(path)
black = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(black,100,200)
dilate = cv2.dilate(canny,kernal,iterations = 2)
erode = cv2.erode(dilate,kernal,iterations = 2)
cv2.imshow("erode",erode)
cv2.waitKey(0)

import cv2
import numpy as np
img = cv2.imread("car.jpeg")
ker = np.ones((7,7),np.uint8)
a = cv2.morphologyEx(img,cv2.MORPH_OPEN,ker)
cv2.imshow('a',a)

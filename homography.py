import cv2
import numpy as np
source = cv2.imread("car.jpeg")
pt1 = np.array([[141,131],[480,159],[493,630],[64,601]])
dest = cv2.imread("car.jpeg")
pt2 = np.array([[318,256],[534,372],[316,670],[73,473]])
h,status = cv2.findHomography(pt1,pt2)
out = cv2.warpPerspective(source,h,(dest.shape[1],dest.shape[0]))
cv2.imshow("sorce",source)
cv2.imshow("destination",dest)
cv2.imshow("warped",out)
cv2.waitKey(0)

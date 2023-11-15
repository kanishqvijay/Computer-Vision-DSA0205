import cv2
path = "ryujin.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image",gray)
cv2.waitKey(0)

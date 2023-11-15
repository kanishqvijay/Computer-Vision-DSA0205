import cv2
path = "car.jpeg"
img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img,100,100)
cv2.imshow("Edge",canny)
cv2.waitKey(0)

import cv2
path = "car.jpeg"
img = cv2.imread(path)
blur = cv2.GaussianBlur(img,(101,101),0)
cv2.imshow("Blur",blur)
cv2.waitKey(0)

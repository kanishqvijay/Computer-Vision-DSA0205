import cv2
path = "car.jpeg"
img =cv2.imread(path)
img = cv2.resize(img,(700,700))
cv2.imshow("image",img)
cv2.waitKey(0)

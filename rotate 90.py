import cv2
path = "car.jpeg"
img =cv2.imread(path)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("image",img)
cv2.waitKey(0)

import cv2
a=cv2.imread("car.jpeg");
Lap=[0, 1, 0, 1, -4, 1, 0, 1, 0];
a1=cv2.conv2(a,Lap,"car.jpeg");
a2=cv2.uint8(a1);
imtool(abs(a-a2),[])
lap=[-1 ,-1, -1, -1, 8, -1, -1, -1 ,-1];
a3=cv2.conv2(a,lap,"car.jpeg");
a4=cv2.uint8(a3);
imtool(abs(a+a4),[])

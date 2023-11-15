import cv2
cap = cv2.VideoCapture(0)
if(cap.isOpened() == False):
    print("Error.")
while(cap.isOpened()):
    ret,frame = cap.read()
    
    cv2.imshow("Frame",frame[:,::-1,:])
    if cv2.waitKey(1000//60) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

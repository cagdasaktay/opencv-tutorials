import cv2
import numpy as np
import datetime

cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3,1920)
#cap.set(4,1080)
#print(cap.get(3))
#print(cap.get(4))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        #text = 'Width:' + str(cap.get(3)) +  '  Height:' + str(cap.get(4)) line 19 da datet yerine text yazarsan width ve height yazılır.
        datet=str(datetime.datetime.now())
        frame= cv2.putText(frame,datet,(30,40),font,1,(0,255,120),3,cv2.LINE_AA)
        cv2.imshow("Video:",frame)
        if cv2.waitKey(20) & 0xFF==ord('q'):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()


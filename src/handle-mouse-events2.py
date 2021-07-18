import cv2
import numpy as np

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: # sol tık ile nokta seçer

        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))

        if len(points) >= 2: #tıklama 2 den fazla ise line çizer
            cv2.line(img,points[-1],points[-2],(255,0,0),5)

        cv2.imshow('Resim:',img)



img=np.zeros((512,512,3),dtype="uint8") #Burada zeros ile fotoğraf yaratabiliriz
#img=cv2.imread("blured.tif") #Fotoğrafı seç
cv2.imshow("Resim:",img)
points= []

cv2.setMouseCallback("Resim:",click_event) #Buradaki "Resim" yazısı imshow daki ile aynı olmak zorunda.
cv2.waitKey(0)
cv2.destroyAllWindows()

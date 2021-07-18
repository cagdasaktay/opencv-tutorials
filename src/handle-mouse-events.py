import cv2
import numpy as np

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: # sol tık ile koordinatları alır
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY= str(x) + ' , ' + str(y)
        cv2.putText(img,strXY,(x,y),font,.5,(255,0,0),1)
        cv2.imshow('Resim:',img)
    if event==cv2.EVENT_RBUTTONDOWN: # sağ tık ile renk kodlarını alır
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ' , ' + str(green)+ ' , ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 0), 1)
        cv2.imshow('Resim:', img)


#img=np.zeros((512,512,3),dtype="uint8") Burada zeros ile fotoğraf yaratabiliriz
img=cv2.imread("chicky_512.png") #Fotoğrafı seç
cv2.imshow("Resim:",img)

cv2.setMouseCallback("Resim:",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()


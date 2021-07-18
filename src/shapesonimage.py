import cv2
import numpy as np

#img=cv2.imread("blured.tif")
img=np.zeros([512,512,3],dtype="uint8")

cv2.line(img,(20,20),(50,50),(0,255,0),3)
cv2.arrowedLine(img,(40,100),(150,150),(255,0,0),3)
cv2.circle(img,(100,100),10,(0,255,0),-1) #Thickness'a (-1) verirsen içi dolar.
cv2.rectangle(img,(0,0),(160,160),(100,100,100),2)
cv2.putText(img,"Cado",(0,80),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,0),2)


cv2.imshow("Resim:",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

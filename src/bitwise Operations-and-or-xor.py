import cv2
import numpy as np

img1=np.zeros((256,256,3),dtype="uint8")
img1=cv2.rectangle(img1,(100,0),(200,100),(255,255,255),-1)
img2=cv2.imread("blured.tif")

#bitAnd=cv2.bitwise_and(img2,img1) # And işlemi (kesişimlerini alır.)
#bitOr=cv2.bitwise_or(img2,img1) # Or işlemi
#bitXor=cv2.bitwise_xor(img2,img1) # Xor işlemi
bitNot=cv2.bitwise_not(img1) #tek parametre
bitNot2=cv2.bitwise_not(img2) #tek parametre

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
#cv2.imshow("And",bitAnd)
#cv2.imshow("Or",bitOr)
#cv2.imshow("Xor",bitXor)
cv2.imshow("Not1",bitNot)
cv2.imshow("Not2",bitNot2)
cv2.waitKey(0)
cv2.destroyAllWindows()

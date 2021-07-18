import cv2 as cv
import numpy as np

img = cv.imread("gradient.png",0)
ret,th1=cv.threshold(img,127,255,cv.THRESH_BINARY) # Siyahı siyah beyazı beyaz yapar 0 ya da 1 mantığı
ret,th2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV) # 2. parametre ilk pixeli,2. parametre kaça kadar gideceğidir.binary tersi(inverse)
ret,th3=cv.threshold(img,127,255,cv.THRESH_TRUNC) # 127 ( yani ilk parametre) pixelden sonraki tüm pixelleri aynı renk yapar
ret,th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)#ilk parametreye kadar 0 yapar, sonrası aynı kalır
ret,th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV) #ilk parametreye kadar aynı sonrası 0, yani siyah olur

cv.imshow("Image",img)
cv.imshow("th1",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)
cv.imshow("th4",th4)
cv.imshow("th5",th5)


cv.waitKey(0)
cv.destroyAllWindows()

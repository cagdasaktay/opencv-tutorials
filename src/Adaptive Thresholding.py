import cv2 as cv
import numpy as np
#adaptive threshold daha küçük bölgeler için kullanılır.
img=cv.imread("sudoku.png",0)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow("Image",img)
cv.imshow("th1",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)

cv.waitKey(0)
cv.destroyAllWindows()
"""if u have color image then first cvtColor to Grayscale then use adaptive thresholding or 
read the color image using: cv2.imread('colored_img.jpg',cv.IMREAD_GRAYSCALE) 
or u can just put flag=0 in the method imread()"""
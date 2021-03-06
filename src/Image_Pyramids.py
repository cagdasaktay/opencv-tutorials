import cv2
import numpy as np

img = cv2.imread("lena.jpg")
"""lr1 = cv2.pyrDown(img) # Boyutu yarıya düşürür.
lr2 = cv2.pyrDown(lr1) # Yarının Yarısı alındı.
hr = cv2.pyrUp(lr2)"""

layer = img.copy()
gp = [layer] #Gaussian

for i in range (6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow("upper level Gaussian Pyramid",layer)
lp = [layer] # Laplacian

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)


cv2.imshow("Original Image",img)

"""cv2.imshow("pyrDown 1 Image",lr1)
cv2.imshow("pyrDown 2 Image",lr2)
cv2.imshow("pyrUp 1 Image",hr)"""

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img=cv2.imread("chicky_512.png")
img2=cv2.imread("graf.png")

print(img.shape) # row, column and channel
print(img.size) # total number of pixel
print(img.dtype) # image datatype

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
noise= img[130:170,200:260] #burun kopyalama (kesit alma)
img[20:60,30:90] =noise #burnu taşıma

img=cv2.resize(img,(512,512)) # yeniden boyutlandırma
img2=cv2.resize(img2,(512,512)) # 2. resmi yenden boyutlandırma

#added=cv2.add(img,img2) #2 resmi üst üste ekleme.(ekleyebilmek için boyutları aynı olması gerek (x,y)
added2=cv2.addWeighted(img,.4,img2,.6,0) # eklemeyi oran ile yapar.

cv2.imshow("Resim:",added2)
cv2.waitKey(0)
cv2.destroyAllWindows()




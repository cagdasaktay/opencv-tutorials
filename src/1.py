import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv2.rectangle(goruntu, (100, 100), (200, 200), (255, 0, 0), 2)
    cv2.line(goruntu, (50, 50), (100, 100), (255, 255, 0), 3)
    cv2.circle(goruntu, (60, 60), 5, (0, 255, 0), 3)
    cv2.putText(goruntu, "Cagdas", (20, 250), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 0, 0), 1)
    cv2.imshow("Video:",goruntu)

    if cv2.waitKey(30) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
import urllib.request
import cv2
import numpy as np
import time
URL = "http://100.93.2.39:8080/shot.jpg"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    cv2.imshow('IPWebcam',img)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break;

    
cv2.destroyAllWindows()

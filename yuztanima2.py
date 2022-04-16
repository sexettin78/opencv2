#BU PROGRAMIN ÇALIŞMASI İÇİN  OPENCV 'haarcascade' DOSYALARINA İHTİYAÇ VARDIR. FOTOĞRAF ÜZERİNDE YÜZ ÇERÇEVELER

import cv2
import numpy as np
face_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("resim.jpg")

griton = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_casc.detectMultiScale(griton,1.1,3) # 3 SAYISINI ARTTIRIRSAN DAHA ÇOK ARAR

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("face",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

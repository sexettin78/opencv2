#BU PROGRAMIN ÇALIŞMASI İÇİN  OPENCV 'haarcascade' DOSYALARINA İHTİYAÇ VARDIR. VİDEO ÜZERİNDE YÜZ VE GÖZ ÇERÇEVELER
import cv2
import numpy as np

cam = cv2.VideoCapture(0) #FARKLI KAMERADA ÇALIŞTIRMAK İÇİN 1, VİDEO DOSYASINDA ÇALIŞTIRMAK İÇİN İSE "videoadi.uzanti" ŞEKLİNDE GİRİNİZ ÖRNEK: cv2.VideoCapture("video.mp4")

while True:
    x,cap = cam.read()

    face_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml
    eye_casc = cv2.CascadeClassifier("haarcascade_eye.xml")#https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_eye.xml

    gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

    faces = face_casc.detectMultiScale(gray,1.1,4)
    eyes = eye_casc.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(cap,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(cap,'face',(x+w-60,y+h+17),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

    for(a,b,c,d) in eyes:
        cv2.rectangle(cap,(a,b),(a+c,b+d),(0,255,0),1)
        cv2.putText(cap,'eye',(a+c-60,b+d+17),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)


    cv2.imshow("goruntu",cap)


    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

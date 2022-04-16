import cv2
import numpy as np
#çerçeve büyüklüğü ayarlıyoruz
frameWidth = 640
frameHeight = 360



cap = cv2.VideoCapture("video1.mp4") #0 yazarsan  kendi kamerandan alırsın 1 yazarsan harici kameran açılır

#videoyu her an resim alıp oynatacağı için (video oynatma mantığı budur.) böyle bir döngü kullanıyoruz.
while True:
    succsess,img = cap.read()
    #çerçevenin büyüklüğünü enjekte etmek
    img=cv2.resize(img,(frameWidth , frameHeight))
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    cv2.imshow("video1",laplacian)

    if cv2.waitKey(25) & 0XFF == ord("q"): #q tuşuna basınca kapansın
        break

#kamerayı kapattık
cap.release()
cv2.destroyAllWindows()





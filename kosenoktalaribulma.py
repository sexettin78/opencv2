import cv2
import numpy as np

img = cv2.imread("resim.jpg")
img_gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)

koseler = cv2.goodFeaturesToTrack(img_gray,60,0.01,10) #burada 60 sayısı, tahmin ettiğimiz 60 tane köşe var demek, buradaki 10 sayısı kaç pixelde bir köşe göreceğimiz.

koseler = np.int0(koseler)

for kose in koseler:
    x,y=kose.ravel()
    cv2.circle(img,(x,y),10,(0,255,0),-1)

cv2.imshow("resim.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

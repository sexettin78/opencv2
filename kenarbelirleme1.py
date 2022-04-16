import cv2
import numpy as np
img = cv2.imread("resim.jpg")

laplacian = cv2.Laplacian(img,cv2.CV_64F)

sobel = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

#sobely = sobelyatay
cv2.imshow("orijinal",img)
cv2.imshow("laplacian",laplacian)
cv2.imshow("sobel",sobel)
cv2.imshow("sobely",sobely)

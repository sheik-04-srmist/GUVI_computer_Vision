import cv2
import numpy as np 
import matplotlib.pyplot as pit    

img =cv2.imread("image 4.jpg")

blur =cv2.blur(img,(5,5))
gaussian=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)

titles=["original","Blur","Gaussian","Median"]
images=[img,blur,gaussian,median]
for i in range(4):
    pit.subplot(2,2,i+1),pit.imshow(images[i]),pit.title(titles[i])
    pit.axis("off")
pit.show()



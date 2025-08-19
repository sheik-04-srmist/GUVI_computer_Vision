
import cv2
import matplotlib.pyplot as pit
img =cv2.imread("istock.jpg")
print(img.shape)
cv2.rectangle(img,(50,50),(100,100),(255,0,0),2)



pit.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
pit.show()



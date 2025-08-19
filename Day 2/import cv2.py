import cv2
import matplotlib.pyplot as pit
img=cv2.imread("IMG.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thereshold,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
hist=cv2.calcHist(gray,[0],None,[256],[0,256])

pit.plot(hist)

pit.show()
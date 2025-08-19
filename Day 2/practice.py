import cv2
import matplotlib.pyplot as pit
img=cv2.imread("download.jpg")

median = cv2.medianBlur(img,3)
pit.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
pit.show()
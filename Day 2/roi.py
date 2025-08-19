
import cv2
import matplotlib.pyplot as pit
img=cv2.imread("IMG.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussian=cv2.GaussianBlur(img,(15,15),0)
edges =cv2.Canny(gray,)
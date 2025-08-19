
import cv2
import matplotlib.pyplot as pit
import numpy as np

img = cv2.imread("eren.webp")
rows,cols=img.shape[:2]
(h,w) = img.shape[:2]

cv2.flip(img,1)

print(img.shape)

cv2.circle(img,(375,375),275,(0,00,400),1)

m = np.float32([[1,0,-300],[0,1,0]])
translate = cv2.warpAffine(img,m,(cols,rows))

RM = cv2.getRotationMatrix2D((w//2,h//2),140,1)
rotated = cv2.warpAffine(img,RM,((w,h)))

pit.imshow(cv2.cvtColor(translate,cv2.COLOR_BGR2RGB))
pit.show()


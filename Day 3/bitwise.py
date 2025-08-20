import cv2
import numpy as np
import matplotlib.pyplot as pit

img = np.zeros((500,500),dtype=np.uint8)
circle = cv2.circle(img.copy(),(250,250),250,(255,255,255),-1)
rect = cv2.rectangle(img.copy(),(50,50),(470,470),(255,255,255),-1)

intersection = cv2.bitwise_xor(circle,rect,None)

pit.imshow(cv2.cvtColor(intersection,cv2.COLOR_BGR2RGB))
pit.show()
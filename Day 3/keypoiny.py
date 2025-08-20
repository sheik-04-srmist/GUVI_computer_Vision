import cv2
import matplotlib.pyplot as pit
img = cv2.imread("building.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#SIFT
sift = cv2.SIFT_create()
keypoints, descriptons = sift.detectAndCompute(gray,None)

img_sift = cv2.drawKeypoints(img,keypoints,None,flags =
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
pit.imshow(cv2.cvtColor(img_sift,cv2.COLOR_BGR2RGB))
pit.axis("off")
pit.show()
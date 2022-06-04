import cv2
import imutils
img = cv2.imread("mimi.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color conversion  - color gray
thresImg = cv2.threshold(grayImg,120,255,cv2.THRESH_BINARY) [1]
cv2.imwrite("thresholdImage4.jpg",thresImg)


import cv2
import imutils

img = cv2.imread("mimi.jpg") #read an image
resizeImg = imutils.resize(img, width=20) #resize an image
cv2.imwrite("resizedImage.jpg",resizeImg) #save imgae

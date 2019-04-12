import cv2
import sys

image = cv2.imread("../assets/closing.jpeg")

#Create structuring element/kernel and select and elliptical kernel
closingSize = 3
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*closingSize + 1, 2*closingSize + 1), (closingSize, closingSize))

#Apply dilation on the image followed by erosion
result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, element)

#Create windows to show images
cv2.namedWindow("input image", cv2.WINDOW_NORMAL)
cv2.namedWindow("closed image", cv2.WINDOW_NORMAL)

#display images
cv2.imshow("input image", image)
cv2.imshow("closed image", result)

#Press esc on keyboard to exit the program
cv2.waitKey(0)

#close all the opened windows
cv2.destroyAllWindows()
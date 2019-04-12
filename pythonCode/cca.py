import cv2
import sys
import numpy as np

#Read image as grayScale over which cca is to be applied
image = cv2.imread("../assets/cca.png", cv2.IMREAD_GRAYSCALE)

#get binary image
th, binaryImage = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

#Find connected components
_, binaryImage=cv2.connectedComponents(binaryImage)

#get clone of binary image to work on so that finally we can compare input and output images
binaryImageClone = np.copy(binaryImage) 

#Find the max and min pixel values and their locations
(minValue, maxValue, minPosition, maxPosition) = cv2.minMaxLoc(binaryImageClone)

#normalize the image so that the min value is 0 and max value is 255
binaryImageClone = 255 * (binaryImageClone - minValue) / (maxValue - minValue)

#convert image to 8bits unsigned type
binaryImageClone = np.uint8(binaryImageClone)

#Apply a color map
binaryImageCloneColorMap = cv2.applyColorMap(binaryImageClone, cv2.COLORMAP_JET)

#Create windows to display images
cv2.namedWindow("input image", cv2.WINDOW_NORMAL)
cv2.namedWindow("cca image", cv2.WINDOW_NORMAL)
cv2.namedWindow("cca image color", cv2.WINDOW_NORMAL)

#Display images
cv2.imshow("input image", image)
cv2.imshow("cca image", binaryImageClone)
cv2.imshow("cca image color", binaryImageCloneColorMap)

#Press esc on keybaord to exit the program
cv2.waitKey(0)

#Close all the opened windows
cv2.destroyAllWindows()
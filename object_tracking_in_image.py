import cv2
import numpy

image = cv2.imread('color.jpg', 1)
cv2.imshow('original', image)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv_image', hsv_image)

lower_bound = numpy.array([100, 150, 20])
upper_bound = numpy.array([130, 255, 255])
mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
# cv2.imshow('mask', mask)

result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('found', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

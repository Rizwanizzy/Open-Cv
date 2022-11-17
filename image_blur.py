import cv2
import numpy

image = cv2.imread('img.jpg', 1)
# matrix=numpy.ones((5,5),numpy.float32)/25
# new_image=cv2.filter2D(image,-5,matrix)
blur = cv2.blur(image, (5, 5))
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('original', image)
# cv2.imshow('blur image',new_image)
cv2.imshow('blur image', blur)
cv2.imshow('Gaussian image', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread('gradient.jpg', 1)
cv2.imshow('original', image)
ret,threshold_image=cv2.threshold(image,150,255,cv2.THRESH_BINARY)
cv2.imshow('processed image',threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread('img.jpg', 1)
cv2.line(img, (0, 0), (650, 450), (5, 5, 5), 4)
cv2.rectangle(img, (50, 35), (200, 140), (0, 0, 255), 2)
cv2.circle(img, (200, 140), 104, (0, 255, 0), 2)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,"hey",(70,100),font,2,(255,255,255),cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

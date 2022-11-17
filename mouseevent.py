import cv2


def draw_circle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 30, (0, 0,255), -1)


img = cv2.imread('img.jpg', 1)
cv2.namedWindow('img')
cv2.setMouseCallback('img', draw_circle)

while 1:
    cv2.imshow('img', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

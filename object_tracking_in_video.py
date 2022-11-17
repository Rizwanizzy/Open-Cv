import cv2
import numpy

capture = cv2.VideoCapture(0)
while 1:
    _, frame = capture.read()
    hsv_video = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = numpy.array([25, 150, 20])
    upper_bound = numpy.array([35, 255, 255])
    mask = cv2.inRange(hsv_video, lower_bound, upper_bound)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('found', result)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cv2.destroyAllWindows()

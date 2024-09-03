#實時鏡頭
import cv2

see = cv2.VideoCapture(0)
see.isOpened()
while(1):
    ret, frame = see.read()
    if ret:
        frame = cv2.resize(frame, (0,0), fx=1.2, fy=1.2)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break

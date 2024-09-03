import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while(1):
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1] 
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                for i, lm in enumerate(handLms.landmark):
                    #position
                    xPos = int(lm.x * imgHeight) 
                    yPos = int(lm.y * imgWidth)
                    cv2.putText(img, 
                                str(i), #號碼
                                (xPos+100,yPos-40), #位置
                                cv2.FONT_HERSHEY_COMPLEX, #字體 
                                0.4, #大小
                                (255,0,0), #顏色
                                2 #粗度
                                )
                    print(i, xPos, yPos)
        cv2.imshow('img', img)
    
    if cv2.waitKey(10) == ord('q'):
        break


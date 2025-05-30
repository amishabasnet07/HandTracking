import cv2
import time
import numpy as np
import HandTrackinModule as htm  # Your custom hand tracking module

# Remove this line
# from MyNewGameHandTracking import lmlist

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)  # ✅ Draw hand landmarks

    lmlist = detector.findPosition(img, draw=True)  # ✅ Optionally draw circle at landmarks

    if lmlist:
        print(lmlist[4])  # Example: Tip of thumb

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 70),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Img", img)
    cv2.waitKey(1)

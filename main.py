import cv2
import mediapipe as mp
import time
from virtualMouse import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector()
pTime = 0
while True:
    success, img = cap.read()
    if not success:
        break

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(
        img,
        f"FPS: {int(fps)}",
        (10, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    img = detector.detect_hands(img)  
    lm_list, img = detector.find_position(img)    
    # img = cv2.flip(img, 1) 
    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
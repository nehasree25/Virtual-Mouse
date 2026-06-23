import cv2
import mediapipe as mp
import time
from handDetector import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector()
while True:
    success, img = cap.read()
    
    if not success:
        break
    img = detector.detect_hands(img)  
    lm_list, img = detector.find_position(img)    
    img = cv2.flip(img, 1) 
    cv2.imshow("Landmark Detection", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
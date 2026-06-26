import cv2
import mediapipe as mp
import pyautogui as pg
mp_hands = mp.solutions.hands
screen_width = pg.size().width
screen_height = pg.size().height

class HandDetector:
    def __init__(self,mode = False, max_hands = 2, detectionCon= 0.5, trackCon = 0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.hands = mp_hands.Hands(
                        static_image_mode=self.mode,
                        max_num_hands=self.max_hands,
                        min_detection_confidence=self.detectionCon,
                        min_tracking_confidence=self.trackCon
                    )
        self.mp_draw = mp.solutions.drawing_utils
        self.index_height = 0


    def detect_hands(self, img, draw = True):
        h, w, c = img.shape

        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb_img)

        if  self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )
                cv2.putText(
                    img,
                    "Virtual Mouse",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )
        return img
    def find_position(self, img, hand_no = 0, draw = True):
        lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id==4:
                    thumb_width = screen_width / w * cx
                    thumb_height = screen_height / h * cy
                    cv2.circle(img, (cx, cy), 15, (255, 255, 0))
                    if abs(thumb_height - self.index_height) < 20:
                        pg.click()
                if id==8:
                    index_width = screen_width / w * cx
                    self.index_height = screen_height / h * cy
                    cv2.circle(img, (cx, cy), 15, (255, 255, 0))
                    pg.moveTo(index_width, self.index_height)

        return lm_list,img
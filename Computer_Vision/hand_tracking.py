import cv2
import mediapipe as mp
import time
import math

class HandTracking:
    def __init__(self, mode= False, max_hands= 1):
        self.__mode__ = mode
        self.__max_hands__ = max_hands

        self.model_hands = mp.solutions.hands.Hands(static_image_mode = self.__mode__,max_num_hands = self.__max_hands__)

        self.drawMP = mp.solutions.drawing_utils

    
    def find_fingers(self, frame, draw = True):
        convert_RGB= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.detect_hand = self.model_hands.process(convert_RGB)
        

        if self.detect_hand.multi_hand_landmarks:
            for hand in self.detect_hand.multi_hand_landmarks:
                if draw:
                    self.drawMP.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
        
        return frame
    

def main(): 
    present_time = 0
    previous_time = 0

    capture = cv2.VideoCapture(0)
    detector = HandTracking()

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


    if not capture.isOpened():
        # Verifica se a câmera foi aberta com sucesso.
            print("Cannot open camera")
            exit()

    while True:
        status, frame = capture.read()
        frame = detector.find_fingers(frame)

        cv2.imshow('frame', frame)
        
        if (not status) or (cv2.waitKey(1) == ord("q")):
            capture.release()
            cv2.destroyAllWindows
            break


if __name__ == "__main__":
            main()
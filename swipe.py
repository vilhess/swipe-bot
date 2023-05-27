from deepface import DeepFace
import numpy as np
import keyboard
import cv2
from PIL import ImageGrab
from time import sleep


def swipe():
    while (not keyboard.is_pressed("esc")):
        sleep(3)
        try:

            image = cv2.cvtColor(np.array(ImageGrab.grab(
                bbox=(765, 180, 1125, 855))), cv2.COLOR_RGB2BGR)  # Adapt the bbox to your screen
            sleep(2)
            result = DeepFace.analyze(image)[0]
            sex = result['dominant_gender']
            emotion = result['dominant_emotion']

            if emotion in ['happy', 'neutral'] and sex == "Woman":
                keyboard.press_and_release('right')

            else:
                keyboard.press_and_release('left')
        except:
            # If the face is not detected, swipe left (or right if you are not complicated)
            keyboard.press_and_release('left')


swipe()

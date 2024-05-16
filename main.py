import cv2
import mediapipe as mp
import numpy as np
from src import draw_hand_landmarks as drawer


def main():
    """main method"""
    vid = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    while True:
        ret, image = vid.read()
        if not ret:
            break
        image = cv2.flip(image, 1)
        hands_image = np.ones(image.shape, dtype = np.uint8)
        hands_image[:, :, :] = 255

        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                image, bounding_rect = drawer.draw_hand_landmarks(image, hand_landmarks)
                hands_image, _ = drawer.draw_hand_landmarks(hands_image, hand_landmarks)

                x1, y1, x2, y2 = bounding_rect
                hands_image[y1:y2, x1:x2, :] = image[y1:y2, x1:x2, :]

        cv2.imshow('image', image)
        cv2.imshow('hands', hands_image)

        input_key = cv2.waitKey(1) & 0xFF
        if input_key == ord('q'): # quit program
            break
        if input_key == ord('t'): # get data and train model
            break
        # elif input_key == ord('l'): # track current letter
        #     break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

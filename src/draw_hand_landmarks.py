import cv2
import numpy as np

BGR_RED = (0, 0, 255)
BGR_GREEN = (0, 255, 0)

def draw_hand_landmarks(image, hand_landmarks):
    """Calculate and draw landmark outputs for hand"""
    brect = calc_bounding_rect(image, hand_landmarks)
    landmark_list = calc_landmark_list(image, hand_landmarks)

    image = draw_bounding_rectangle(image, brect)
    image = draw_landmarks(image, landmark_list)

    return image, brect

def calc_bounding_rect(image, landmarks):
    """Calculates the bounding box for the hand"""
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_array = np.empty((0, 2), int)

    for landmark in landmarks.landmark:
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)

        landmark_point = [np.array((landmark_x, landmark_y))]

        landmark_array = np.append(landmark_array, landmark_point, axis=0)

    x, y, w, h = cv2.boundingRect(landmark_array)
    return [x, y, x + w, y + h]

def calc_landmark_list(image, landmarks):
    """Calculates the exacts points for each landmark"""
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_point = []

    for landmark in landmarks.landmark:
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)

        landmark_point.append([landmark_x, landmark_y])

    return landmark_point

def draw_bounding_rectangle(image, brect):
    """Draw bounding rectangle on image around the detected hand"""
    cv2.rectangle(image, (brect[0], brect[1]), (brect[2], brect[3]),
               (0, 0, 0), 1)
    return image

def draw_landmarks(image, landmark_point):
    """Draw Landmarks onto image for detected hand"""
    if len(landmark_point) > 0:
        # Thumb
        cv2.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]),
                BGR_GREEN, 2)

        # Index finger
        cv2.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]),
                BGR_GREEN, 2)

        # Middle finger
        cv2.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]),
                BGR_GREEN, 2)

        # Ring finger
        cv2.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]),
                BGR_GREEN, 2)

        # Little finger
        cv2.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]),
                BGR_GREEN, 2)

        # Palm
        cv2.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[0]), tuple(landmark_point[5]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[0]), tuple(landmark_point[9]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[0]), tuple(landmark_point[13]),
                BGR_GREEN, 2)
        cv2.line(image, tuple(landmark_point[0]), tuple(landmark_point[17]),
                BGR_GREEN, 2)

    # Key Points
    for landmark in landmark_point:
        cv2.circle(image, (landmark[0], landmark[1]), 5, BGR_RED, -1)

    return image

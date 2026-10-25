
import os
import time
import urllib.request
from datetime import datetime
from pathlib import Path

import cv2
import mediapipe as mp
import numpy as np

try:
    from mediapipe.tasks.python.core.base_options import BaseOptions
    from mediapipe.tasks.python.vision.core.vision_task_running_mode import (
        VisionTaskRunningMode,
    )
except ImportError:
    from mediapipe.tasks.python import BaseOptions
    from mediapipe.tasks.python.vision import RunningMode as VisionTaskRunningMode

from mediapipe.tasks.python.vision import HandLandmarker, HandLandmarkerOptions

MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
    "hand_landmarker/float16/1/hand_landmarker.task"
)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "hand_landmarker.task")
PHOTO_DIR = Path.home() / "Pictures" / "Gesture-Controlled-Photos"
PHOTO_DIR.mkdir(parents=True, exist_ok=True)


def ensure_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading hand landmark model...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    return MODEL_PATH


model_path = ensure_model()
hand_landmarker = HandLandmarker.create_from_options(
    HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionTaskRunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.7,
        min_hand_presence_confidence=0.7,
        min_tracking_confidence=0.7,
    )
)

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17), (1, 5), (9, 13)
]

filters = [
    None,
    'GRAYSCALE',
    'SEPIA',
    'NEGATIVE',
    'BLUR'
]

current_filter = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

last_action_time = 0
debounce_time = 1


def apply_filter(frame, filter_type):
    if filter_type == 'GRAYSCALE':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif filter_type == 'SEPIA':
        sepia_filter = np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ], dtype=np.float32)

        sepia_frame = cv2.transform(frame, sepia_filter)
        sepia_frame = np.clip(sepia_frame, 0, 255)
        return sepia_frame.astype(np.uint8)

    elif filter_type == 'NEGATIVE':
        return cv2.bitwise_not(frame)

    elif filter_type == 'BLUR':
        return cv2.GaussianBlur(frame, (15, 15), 0)

    return frame


def render_filter(frame, filter_type):
    filtered_frame = apply_filter(frame, filter_type)
    if filter_type == 'GRAYSCALE':
        return cv2.cvtColor(filtered_frame, cv2.COLOR_GRAY2BGR)
    return filtered_frame


def draw_hand_landmarks(img, landmarks):
    for connection in HAND_CONNECTIONS:
        start = landmarks[connection[0]]
        end = landmarks[connection[1]]
        start_x = int(start.x * img.shape[1])
        start_y = int(start.y * img.shape[0])
        end_x = int(end.x * img.shape[1])
        end_y = int(end.y * img.shape[0])
        cv2.line(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

    for landmark in landmarks:
        x = int(landmark.x * img.shape[1])
        y = int(landmark.y * img.shape[0])
        cv2.circle(img, (x, y), 5, (255, 0, 0), cv2.FILLED)


while True:
    success, img = cap.read()

    if not success:
        print("Failed to read frame from webcam.")
        break

    img = cv2.flip(img, 1)
    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    results = hand_landmarker.detect_for_video(mp_image, int(time.time() * 1000))

    if results and results.hand_landmarks:
        for landmarks in results.hand_landmarks:
            draw_hand_landmarks(img, landmarks)

            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            middle_tip = landmarks[12]
            ring_tip = landmarks[16]
            pinky_tip = landmarks[20]

            frame_height, frame_width, _ = img.shape

            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)
            index_x = int(index_tip.x * frame_width)
            index_y = int(index_tip.y * frame_height)
            middle_x = int(middle_tip.x * frame_width)
            middle_y = int(middle_tip.y * frame_height)
            ring_x = int(ring_tip.x * frame_width)
            ring_y = int(ring_tip.y * frame_height)
            pinky_x = int(pinky_tip.x * frame_width)
            pinky_y = int(pinky_tip.y * frame_height)

            cv2.circle(img, (thumb_x, thumb_y), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (middle_x, middle_y), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (ring_x, ring_y), 10, (255, 255, 0), cv2.FILLED)
            cv2.circle(img, (pinky_x, pinky_y), 10, (255, 0, 255), cv2.FILLED)

            current_time = time.time()

            if (
                abs(thumb_x - index_x) < 30
                and abs(thumb_y - index_y) < 30
            ):
                if current_time - last_action_time > debounce_time:
                    cv2.putText(
                        img,
                        "Picture Captured!",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )

                    photo_path = PHOTO_DIR / (
                        f"picture_{datetime.now():%Y%m%d_%H%M%S_%f}.jpg"
                    )
                    capture_img = render_filter(img, filters[current_filter])
                    if cv2.imwrite(str(photo_path), capture_img):
                        last_action_time = current_time
                        print(f"Picture saved to: {photo_path}")
                    else:
                        print(f"Error: Could not save picture to {photo_path}")

            elif (
                (
                    abs(thumb_x - middle_x) < 30
                    and abs(thumb_y - middle_y) < 30
                )
                or (
                    abs(thumb_x - ring_x) < 30
                    and abs(thumb_y - ring_y) < 30
                )
                or (
                    abs(thumb_x - pinky_x) < 30
                    and abs(thumb_y - pinky_y) < 30
                )
            ):
                if current_time - last_action_time > debounce_time:
                    current_filter = (current_filter + 1) % len(filters)
                    last_action_time = current_time
                    print(f"Switched to filter: {filters[current_filter]}")

    filtered_img = render_filter(img, filters[current_filter])
    cv2.imshow("Gesture-Controlled Photo App", filtered_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
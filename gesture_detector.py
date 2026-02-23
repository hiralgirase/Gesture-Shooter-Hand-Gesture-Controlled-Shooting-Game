import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        BaseOptions = mp.tasks.BaseOptions
        HandLandmarker = mp.tasks.vision.HandLandmarker
        HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        options = HandLandmarkerOptions(
            base_options=BaseOptions(
                model_asset_path="hand_landmarker.task"
            ),
            running_mode=VisionRunningMode.IMAGE,
            num_hands=1
        )

        self.detector = HandLandmarker.create_from_options(options)

    def get_gesture(self):
        success, frame = self.cap.read()
        if not success:
            return None, None

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        result = self.detector.detect(mp_image)

        if result.hand_landmarks:
            landmarks = result.hand_landmarks[0]

            index_tip = landmarks[8]
            index_pip = landmarks[6]
            middle_tip = landmarks[12]
            middle_pip = landmarks[10]

            hand_x = index_tip.x

            if (index_tip.y > index_pip.y and
                middle_tip.y > middle_pip.y):
                return "FIST", hand_x

            return None, hand_x

        return None, None

    def release(self):
        self.cap.release()
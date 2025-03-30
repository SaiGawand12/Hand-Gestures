import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)
zoom_factor = 1.0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    finger_count = 0
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            
            finger_tips = [4, 8, 12, 16, 20]  # Thumb and four fingers
            finger_states = []
            
            for tip in finger_tips:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    finger_states.append(1)
                else:
                    finger_states.append(0)
            
            finger_count = sum(finger_states)
    
    if finger_count == 1:
        zoom_factor /= 1.1  # Zoom out
    elif finger_count == 2:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    elif finger_count == 3:
        frame = cv2.GaussianBlur(frame, (15, 15), 0)
    elif finger_count == 4:
        frame = cv2.bitwise_not(frame)  # Color inversion
    elif finger_count == 5:
        zoom_factor = 1.0  # Reset
    
    zoomed_frame = cv2.resize(frame, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)
    center_x, center_y = zoomed_frame.shape[1] // 2, zoomed_frame.shape[0] // 2
    crop_x, crop_y = w // 2, h // 2
    cropped_frame = zoomed_frame[max(0, center_y - crop_y):min(zoomed_frame.shape[0], center_y + crop_y),
                                 max(0, center_x - crop_x):min(zoomed_frame.shape[1], center_x + crop_x)]
    
    cv2.imshow("Hand Gesture Control", cropped_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
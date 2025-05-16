import cv2
import mediapipe as mp
import pygame
import numpy as np
import os
import time

# Initialize Pygame for music
pygame.mixer.init()

# Load songs from folder
song_folder = "songs"
songs = [os.path.join(song_folder, song) for song in os.listdir(song_folder) if song.endswith(".mp3")]
song_index = 0

# Load first song
if songs:
    pygame.mixer.music.load(songs[song_index])

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)


# Function to calculate distance between two points
def calc_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


# Start capturing video
cap = cv2.VideoCapture(0)
last_gesture = None
last_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip image for mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark points
            landmarks = [(int(l.x * w), int(l.y * h)) for l in hand_landmarks.landmark]

            # Thumb tip & index finger tip
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]

            # Check distance between thumb and index finger for volume control
            volume = calc_distance(thumb_tip, index_tip) / 100
            volume = min(max(volume, 0), 1)  # Clamp between 0 and 1
            pygame.mixer.music.set_volume(volume)

            # Palm open (play) / Fist (pause)
            if calc_distance(landmarks[5], landmarks[17]) > 100:  # Open hand
                if last_gesture != "play":
                    pygame.mixer.music.play()
                    last_gesture = "play"
            else:  # Fist
                if last_gesture != "pause":
                    pygame.mixer.music.pause()
                    last_gesture = "pause"

            # Swipe right → Next track
            if landmarks[4][0] - landmarks[0][0] > 100 and time.time() - last_time > 1:
                song_index = (song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[song_index])
                pygame.mixer.music.play()
                last_time = time.time()

            # Swipe left → Previous track
            if landmarks[0][0] - landmarks[4][0] > 100 and time.time() - last_time > 1:
                song_index = (song_index - 1) % len(songs)
                pygame.mixer.music.load(songs[song_index])
                pygame.mixer.music.play()
                last_time = time.time()

    # Show video feed
    cv2.putText(frame, "Gesture Controlled Music Player", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Hand Gesture Music Control", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import pygame
import random
import os

# Load pre-trained mood detection model (Ensure correct path)
model = tf.keras.models.load_model("emotions.h5")  # Replace with actual model path

# Initialize face detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)

# Initialize Pygame for music playback
pygame.mixer.init()

# Define mood-to-music mapping (Ensure corresponding directories exist)
mood_music = {
    "Happy": "music/happy/",
    "Sad": "music/sad/",
    "Angry": "music/angry/",
    "Neutral": "music/neutral/",
    "Fear": "music/fear/",
    "Surprise": "music/surprise/",
    "Disgust": "music/disgust/"
}


# Function to detect mood
def detect_mood(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(frame_rgb)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            h, w, c = frame.shape
            x, y, width, height = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)

            face_img = frame[y:y + height, x:x + width]  # Crop face
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            face_img = cv2.resize(face_img, (48, 48))  # Resize to 48x48
            face_img = face_img / 255.0  # Normalize
            face_img = np.expand_dims(face_img, axis=0)  # Add batch dimension
            face_img = np.expand_dims(face_img, axis=-1)  # Add channel dimension

            prediction = model.predict(face_img)
            mood_label = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise'][np.argmax(prediction)]
            return mood_label

    return "Neutral"


# Function to play music based on mood
def play_music(mood):
    if mood in mood_music:
        folder = mood_music[mood]
        if os.path.exists(folder):
            songs = [f for f in os.listdir(folder) if f.endswith(".mp3")]
            if songs:
                song = random.choice(songs)
                pygame.mixer.music.load(os.path.join(folder, song))
                pygame.mixer.music.play()
            else:
                print(f"No songs found for mood: {mood}")
        else:
            print(f"Music folder not found: {folder}")


# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    mood = detect_mood(frame)
    cv2.putText(frame, f"Mood: {mood}", (frame.shape[1] // 2 - 100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
    cv2.imshow("Mood Detector", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('p'):  # Press 'P' to play music
        play_music(mood)
    elif key == ord('q'):  # Press 'Q' to quit
        break

cap.release()
cv2.destroyAllWindows()

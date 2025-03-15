import os
import cv2
import face_recognition
import numpy as np
from datetime import datetime

ALERT_COOLDOWN = 10  # Min seconds between alerts
last_alert_time = datetime.now()

def load_known_faces(directory="known_faces"):
    """
    Loads known face images from a directory and extracts their encodings.
    Returns:
        - known_face_encodings: List of face encodings
        - known_face_names: List of corresponding names
    """
    known_face_encodings = []
    known_face_names = []
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    for file in os.listdir(directory):
        img_path = os.path.join(directory, file)
        try:
            img = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(img)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(os.path.splitext(file)[0])
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    return known_face_encodings, known_face_names

def detect_faces(frame, known_face_encodings, known_face_names, intruder_dir="intruders"):
    """
    Detects faces in a frame and matches them with known encodings.
    If unknown, stores image in 'intruders/' directory.

    Returns:
        - frame with drawn rectangles and labels
        - detected names list
        - saved intruder image path (if applicable)
    """
    global last_alert_time
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
    
    detected_names = []
    intruder_image_path = None

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        else:
            # Save intruder image
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            os.makedirs(intruder_dir, exist_ok=True)
            intruder_image_path = f"{intruder_dir}/{timestamp}.jpg"
            cv2.imwrite(intruder_image_path, frame)

            # Alert cooldown
            current_time = datetime.now()
            if (current_time - last_alert_time).total_seconds() > ALERT_COOLDOWN:
                last_alert_time = current_time

        detected_names.append(name)
        
        # Draw rectangle
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    return frame, detected_names, intruder_image_path

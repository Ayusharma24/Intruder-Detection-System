import streamlit as st
import cv2
import os
from face_utils import load_known_faces, detect_faces
from email_alerts import send_alert, verify_email

st.set_page_config(page_title="Intruder Detection System", layout="centered", page_icon="🔒")
st.title("🔒 Intruder Detection System")
st.subheader("Live Face Recognition with OpenCV")

# Email Verification
recipient_email = st.text_input("Enter recipient email for alerts:")
if st.button("Verify Email"):
    if recipient_email:
        verification_code = verify_email(recipient_email)
        st.session_state["verification_code"] = verification_code
        st.session_state["email_verified"] = False
        st.success("Verification code sent. Check your email.")
    else:
        st.error("Please enter an email address.")

verification_code_input = st.text_input("Enter verification code:")
if st.button("Submit Verification"):
    if verification_code_input == st.session_state.get("verification_code"):
        st.session_state["email_verified"] = True
        st.success("Email verified successfully!")
    else:
        st.error("Incorrect verification code.")

# Load known faces
known_face_encodings, known_face_names = load_known_faces()

if st.button("Start Recognition") and st.session_state.get("email_verified"):
    st.write("Starting face recognition...")
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image")
            break

        processed_frame, detected_names, intruder_image_path = detect_faces(frame, known_face_encodings, known_face_names)

        if "Unknown" in detected_names and recipient_email:
            send_alert("🚨 Intruder Alert!", "An unknown person has been detected!", recipient_email, intruder_image_path)
            st.warning("🚨 Intruder Alert: Unknown person detected!")

        st.image(processed_frame, channels="BGR")

    cap.release()
    cv2.destroyAllWindows()
else:
    st.warning("Please verify your email before starting recognition.")

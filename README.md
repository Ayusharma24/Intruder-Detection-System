Intruder Detection System 🚀

Welcome to the Intruder Detection System, a real-time face recognition application built with OpenCV, Face Recognition, and Streamlit. This application helps in identifying known individuals and detecting intruders, sending alerts via email when an unknown person is detected.

📌 Features

Real-time Face Recognition using OpenCV

Automatic Intruder Detection and alert system

Email Verification before sending alerts

Customizable Face Database for known individuals

Secure Email Alerting with image attachments

🛠️ Installation

1️⃣ Prerequisites

Ensure you have Python 3.8+ installed.

2️⃣ Clone the Repository

git clone https://github.com/Ayusharma24/Intruder-Detection-System.git
cd intruder-detection

3️⃣ Install Dependencies

pip install -r requirements.txt

📂 Setting Up Directories

The application requires two key directories, which need to be created manually by the user:

🔹 known_faces/ (For Known Individuals)

This directory should contain images of authorized individuals. The filenames (without extensions) will be used as labels.

📌 Steps to Set Up:

Manually create the directory inside the project:

mkdir known_faces

Add face images of known people in .jpg, .png, or .jpeg format.

Ensure each file is named as the person's full name (e.g., John_Doe.jpg).

🔹 intruders/ (For Detected Intruders)

This directory will store images of unknown individuals detected by the system.

📌 Steps to Set Up:

Manually create the directory inside the project:

mkdir intruders

No need to add files; the system will automatically save intruder images here.

🚀 Running the Application

After setting up everything, start the application with:

streamlit run app.py

This will open the application in your web browser.

📧 Email Alert Configuration

Set up email alerts by providing your SMTP credentials as environment variables:

export SMTP_EMAIL_ADDRESS="your-email@example.com"
export SMTP_EMAIL_PASSWORD="your-password"
export SMTP_SERVER="smtp.example.com"
export SMTP_PORT="587"

Ensure that your SMTP provider allows third-party access.

🛠️ User Interaction Guide

Face Database Setup: Add authorized individuals' images in known_faces/.

Starting the System: Run streamlit run app.py and follow the interface.

Email Verification: Users must verify their email before receiving alerts.

Intruder Detection: When an unknown face is detected, it is saved in intruders/, and an email is sent.

🛠️ Missing Components (To Be Created by the User)

Certain files and configurations need to be set up by the user:

known_faces/ and intruders/ directories: Must be created manually.

Email credentials: Users must configure their own SMTP settings.

Face Database: Users must upload images of known individuals.

These steps ensure that the system operates correctly without exposing sensitive data.

🛠️ Troubleshooting

Camera not working? Check if another application is using it.

Emails not sending? Verify SMTP credentials and server configuration.

Faces not recognized? Ensure known_faces/ has clear images of individuals.

🤝 Contributing

We welcome contributions! Fork the repository, enhance features, fix bugs, and submit a pull request to make this project even better. 🚀

📜 License

This project is open-source and available under the GNU General Public License v3.0.

📬 Contact

For any queries, reach out via:

📧 Email: alpha992k80@gmail.com
🐙 GitHub Issues: Open an Issue

💡 Let's build AI-powered security solutions together! 🚀

Happy Coding! 🎉


# Driver-Drowsiness-Detection
🚗  **Driver Drowsiness Detection System**

This repository contains an end-to-end computer vision project designed to detect driver drowsiness in real time using webcam input. The system processes facial landmarks to determine eye closure and triggers an alarm when signs of fatigue are detected.
The project demonstrates a complete pipeline — from real-time video capture to alert generation.

📌 **Project Overview**

The goal of this project is to create a safety-focused application that alerts drivers when they show signs of drowsiness, helping reduce road accidents.

Using OpenCV, dlib, and facial landmark detection, the system continuously monitors the driver’s eyes and calculates the Eye Aspect Ratio (EAR) to detect prolonged eye closure.

The alarm is triggered automatically when the EAR falls below a threshold for multiple consecutive frames.

🎯**Project Objectives**

This project follows the steps below:

Real-Time Video Capture: Captures webcam footage for live monitoring.

Face & Eye Detection: Detects the face using dlib’s HOG-based detector.

Facial Landmark Extraction: Maps 68 facial landmark points using a pre-trained model.

EAR Calculation: Computes Eye Aspect Ratio to determine eye openness.

Drowsiness Detection Logic: Checks EAR over consecutive frames to detect fatigue.

Audio Alert: Plays an alarm sound if drowsiness is detected.

User Interaction: Displays real-time output with EAR and live detection results.

🛠**Technical Aspects**
Computer Vision Pipeline

Libraries Used: OpenCV, dlib

Model Used: shape_predictor_68_face_landmarks.dat

Key Technique: Eye Aspect Ratio (EAR)

# Inputs

Live video stream from webcam

**Outputs**

Audio alarm when drowsiness is detected

Visual feedback on the video feed

📁 **Required Files**

The project requires the following assets:

shape_predictor_68_face_landmarks.dat
Facial landmark prediction model — place inside:

models/


music.wav
Alarm sound — place inside:

assets/

🧩** How to Use**
Prerequisites

Make sure the following are installed:

Python 3.x

OpenCV

dlib

imutils

pygame

numpy

scipy

Or install all dependencies using:

pip install -r requirements.txt

📥 **Installation**
1. Clone this repository:
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Install dependencies:
pip install -r requirements.txt

3. Add required files:

Download the facial landmark model:
👉 http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

Extract and place it here:

models/


Place alarm audio file here:

assets/

▶️ Run the Application
python drowsiness.py


OpenCV will activate your webcam and start monitoring for drowsiness.
Press q to exit.

## **📂 Project Structure**

```
├── drowsiness.py
├── README.md
├── requirements.txt
├── models/
│   └── shape_predictor_68_face_landmarks.dat
└── assets/
    └── music.wav
```

    

☁️ **Deployment (Optional)**

Although this project runs primarily on a local machine (due to webcam access), it can be extended using:

Flask Web App

Streamlit App

Desktop GUI (Tkinter/PyQt)

Deployment on cloud platforms like Heroku may not support live webcam streaming, but you can adapt the project for image/video uploads.

🚀 **Future Enhancements**

Add face recognition for personalized alerts

Implement yawning detection

Add dashboard to display EAR, frame statistics, and alert logs

Improve UI/UX with a desktop-based GUI

Develop a mobile or IoT version

Integrate deep learning models for eye-state classification

🤝 **Contributing**

Contributions are always welcome!

You can contribute by:

Submitting issues

Improving documentation

Adding new features

Optimizing code

For major changes, please open an issue first to discuss your ideas.

🙏 **Acknowledgments**

dlib Documentation

OpenCV Documentation

Research papers on Eye Aspect Ratio (EAR)

Python & Computer Vision Community

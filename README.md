# ✋ Air Calculator - Hand Gesture Based Calculator using OpenCV and CVZone

This project is an **Air Calculator** that uses your **hand gestures** to input numbers and operators via your webcam. It is built using **OpenCV**, **CVZone**, and the **HandTrackingModule**.

## 📸 Demo

![Air Calculator Demo] <!-- Replace with your own demo GIF or screenshot -->

## 🚀 Features

- Real-time hand tracking
- Gesture-based number & operator input
- Live evaluation of expressions
- Clear display and gesture instructions
- Smooth and responsive UI

## ✨ Gestures

 Gesture             Action                     
----------------    ----------------------------
 👆 Index Finger    Input Numbers (0–9)        
 ✌️ Index + Middle  Input Operators (+ - * /) 
 👍 Thumb Up        Evaluate expression        
 ✊ Fist            Clear expression           

## 🛠️ Requirements

- Python 3.7+
- OpenCV
- cvzone
- mediapipe

🚀 Getting Started
1. Clone the Repository
   https://github.com/MansiKarki/Air-Calculator-.git
   cd Air-Calculator

3. Install Dependencies
Make sure Python 3.7+ is installed.
   pip install opencv-python pygame cvzone

If cvzone is not found, install directly from GitHub:
   pip install git+https://github.com/cvzone/cvzone.git


🎯 Visual UI Feedback
1. Numbers and operators are shown on screen.
2. Expression and result update live.
3. A delay system avoids multiple inputs on hold.

🛑 Exit Instructions
Press q on your keyboard to quit the application safely.
This releases the webcam and MIDI resources.



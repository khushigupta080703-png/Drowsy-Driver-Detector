# Drowsy-Driver-Detector

## 🗓️ Daily Progress

### Day 1 — April 13, 2026 ✅
- Created project folder structure
- Set up Python virtual environment
- Installed all libraries: OpenCV, dlib, Flask, React
- Pushed first commit to GitHub

**What I learned today:**
- How to set up a Python virtual environment
- How pip and requirements.txt work
- Basic Git commands: init, add, commit, push

- git add README.md
git commit -m "docs: Day 1 progress update in README"
git push

# Drowsy Driver Detector 🚗💤

> Real-time drowsiness detection using Computer Vision + ML + Full Stack

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![Flask](https://img.shields.io/badge/Flask-2.x-red)
![React](https://img.shields.io/badge/React-18-cyan)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

---

## 🚨 Problem
Over **1.5 million road accidents** happen every year due to drowsy driving.
Drivers often don't realize they are falling asleep at the wheel.

## ✅ Solution
A webcam-based system that:
- Detects eye closure in real-time using ML
- Calculates Eye Aspect Ratio (EAR)
- Triggers an alarm when drowsiness is detected
- Shows a live dashboard with stats
- Sends SMS alert via Twilio
- Generates AI safety report

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| ML / CV | Python, OpenCV, dlib |
| Backend | Flask, WebSockets |
| Frontend | React, Tailwind CSS |
| AI Report | Claude API |
| SMS Alert | Twilio |
| Database | SQLite + CSV logs |

---

## 📁 Project Structure

drowsy-driver-detector/
│
├── backend/
│   ├── detector.py        ← Main ML detection
│   ├── app.py             ← Flask API
│   ├── event_logger.py    ← CSV logging
│   └── requirements.txt
│
├── frontend/
│   └── src/
│       └── App.jsx        ← React Dashboard
│
├── logs/
│   └── drowsy_log.csv     ← Event logs
│
└── README.md

---

## 🗓️ 20-Day Progress

| Day | Task | Status |
|-----|------|--------|
| Day 1 | Project setup + GitHub | ✅ Done |
| Day 2 | Webcam feed with OpenCV | ✅ Done |
| Day 3 | Face detection | ⏳ |
| Day 4 | Facial landmarks | ⏳ |
| Day 5 | EAR formula | ⏳ |
| Day 6 | Drowsiness alert | ⏳ |
| Day 7 | Alarm sound | ⏳ |
| Day 8 | Code cleanup | ⏳ |
| Day 9 | Event logging | ⏳ |
| Day 10 | Accuracy testing | ⏳ |
| Day 11 | Flask API | ⏳ |
| Day 12 | WebSockets | ⏳ |
| Day 13 | React dashboard | ⏳ |
| Day 14 | Charts & stats | ⏳ |
| Day 15 | Event history | ⏳ |
| Day 16 | UI polish | ⏳ |
| Day 17 | AI safety report | ⏳ |
| Day 18 | SMS alerts | ⏳ |
| Day 19 | Cloud deploy | ⏳ |
| Day 20 | Final README | ⏳ |

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/drowsy-driver-detector

# Go to backend
cd drowsy-driver-detector/backend

# Install dependencies
pip install -r requirements.txt

# Run detector
python detector.py
```

---

## 👨‍💻 Author



Built in 20 days as a portfolio project.
Following #100DaysOfCode challenge.

---

## 📸 Day 2 — Webcam Feed

### What I built
A live webcam feed using OpenCV that displays:
- Real-time FPS counter
- Frame counter
- Status label (AWAKE / DROWSY)
- Mirror flip for natural feel

### Code snippet
```python
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame = cv2.flip(frame, 1)
cv2.imshow("Drowsy Driver Detector", frame)
```

### What I learned
- How OpenCV captures webcam frames
- What BGR color format means
- How to calculate FPS
- How cv2.putText() draws on frames
- 

# 🤖 AI Object Detection System

A real-time **AI Object Detection System** built with **Python, YOLO (Ultralytics), and OpenCV**.

The project can detect objects from images and through a webcam in real time.

## ✨ Features

* 📷 Object detection from images
* 🎥 Real-time webcam object detection
* 🤖 YOLO11 Nano model
* ⚡ GPU acceleration when available
* 🎯 Configurable confidence threshold
* 🖼️ Support for multiple images in a dataset folder
* 📊 Displays detected object names and confidence scores

## 🛠️ Technologies Used

* Python
* Ultralytics YOLO
* OpenCV
* PyTorch
* NumPy

## 📁 Project Structure

```text
AI-Object-Detection-System/
│
├── dataset/
│   └── images/
│       └── your-images.jpg
│
├── detect.py
├── webcam.py
├── yolo11n.pt
├── requirements.txt
├── README.md
└── venv/
```

> `venv/` should not be uploaded to GitHub. Add it to `.gitignore`.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Ai-Object-Detection-System.git
cd Ai-Object-Detection-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 🖼️ Image Detection

Place your images inside:

```text
dataset/images/
```

Then run:

```bash
python detect.py
```

The program processes the images and prints detected objects with their confidence scores.

## 🎥 Webcam Detection

Run:

```bash
python webcam.py
```

The webcam will open and YOLO will detect objects in real time.

Press:

```text
Q
```

to close the webcam window.

## 🚀 Model

This project currently uses:

```text
yolo11n.pt
```

The model is provided by Ultralytics YOLO.

For custom object detection, the project can later be extended by creating a labeled dataset and training a custom YOLO model.

## 📌 Future Improvements

* [ ] Train a custom YOLO model
* [ ] Add custom object classes
* [ ] Improve real-time detection speed
* [ ] Add object tracking
* [ ] Add detection history
* [ ] Add a graphical user interface
* [ ] Add custom dataset annotation tools

## 👨‍💻 Author

**Supriya Malakar**

GitHub: [@SupriyaMalakar007](https://github.com/SupriyaMalakar007)

---

⭐ If you find this project useful, consider giving it a star!

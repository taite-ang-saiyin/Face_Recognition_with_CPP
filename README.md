### 📄 **Project Description**

**Title**: Real-Time Face Detection and Recognition System using OpenCV and Eigenfaces/Fisherfaces

This project is a complete C++ application built with OpenCV to perform face detection and recognition. The system captures face images from a webcam, stores them in a dataset, trains a face recognition model (using Eigenfaces or Fisherfaces), and performs real-time recognition using a webcam feed.

The project makes use of the **Haar Cascade Classifier** for face detection and **OpenCV's FaceRecognizer API** for training and predicting faces. It allows users to:
- Add their face to the dataset.
- Train the model using collected face images.
- Recognize faces in real-time using a webcam.

---

### 📁 **Directory Structure**
```
FaceRecognitionProject/
│
├── haarcascade_frontalface_alt.xml        # Haar cascade classifier for face detection
├── eigenface.yml                          # Trained face recognition model (output)
├── Faces/                                 # Directory containing face image dataset
├── main.cpp                               # Source code file
├── README.md                              # Project documentation
```

---

### 📦 **Dependencies**
- C++ (C++11 or later)
- OpenCV 3.x or 4.x
- A webcam or USB camera
- Haar Cascade XML files (from OpenCV)

---

### 🔧 **Setup Instructions**

1. **Install OpenCV:**
   - Download and install OpenCV from [https://opencv.org/releases](https://opencv.org/releases).
   - Make sure to set up your compiler and linker paths correctly.

2. **Clone or Download this Repository.**

3. **Directory Preparation:**
   - Ensure the following directories exist:
     ```
     D:\UIT\First Year\Second sem\C++\Face Recognition Project\Faces\
     ```
   - Replace paths in the code with your actual working directory if needed.

4. **Ensure haarcascade XML is in the correct location:**
   - File: `haarcascade_frontalface_alt.xml`
   - Path (update if different):  
     ```
     D:\UIT\First Year\Second sem\C++\C++ project 2\opencv\sources\data\haarcascades_cuda\
     ```

---

### ▶️ **How to Use**

#### 1. Add a New Face
- Function: `addFace()`
- Prompts user to enter their name and captures 10 face images.
- Saves them to the `Faces/` directory for training.

#### 2. Train the Face Recognizer
- Function: `eigenFaceTrainer()`
- Reads images from `Faces/` and trains the recognizer.
- Saves the trained model to `eigenface.yml`.

#### 3. Run Real-Time Face Recognition
- Function: `FaceRecognition()`
- Loads the trained model.
- Captures frames from webcam and identifies faces.
- Draws rectangles and labels on recognized faces in the video feed.

---

### 🧠 **Techniques Used**

- **Face Detection**: Haar Cascade Classifier
- **Face Recognition**:  
  - **EigenFaceRecognizer**
  - **FisherFaceRecognizer**
- **Image Preprocessing**: Grayscale conversion, histogram equalization, image resizing
- **OpenCV GUI**: `imshow`, `waitKey`, real-time camera feed

---

### 📝 **Notes**
- Make sure webcam access is allowed and available.
- Confidence scores help indicate how sure the system is about its predictions.
- Pathnames are hardcoded; consider updating to be more dynamic or use config files.

---

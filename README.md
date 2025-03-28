Sure! Here's the full **Markdown-formatted README code** you can paste directly into your `README.md` file:

```markdown
# 👤 Face Recognition System using OpenCV (C++)

A real-time face detection and recognition system using OpenCV, Haar Cascade classifiers, and Eigenfaces/Fisherfaces algorithms. This project allows you to add new faces, train a recognition model, and recognize faces through your webcam.

---

## 📁 Directory Structure

```
FaceRecognitionProject/
│
├── haarcascade_frontalface_alt.xml        # Haar cascade file for face detection
├── eigenface.yml                          # Trained face recognition model (output)
├── Faces/                                 # Folder to store captured face images
├── main.cpp                               # Main source code
├── README.md                              # Project documentation
```

---

## 🔧 Requirements

- C++11 or later
- OpenCV 3.x or 4.x
- Webcam (built-in or USB)
- Haar cascade XML from OpenCV data

---

## 💻 Setup

1. **Install OpenCV**
   - Download and install OpenCV: https://opencv.org/releases
   - Link OpenCV libraries correctly in your IDE (e.g., Visual Studio, Code::Blocks, etc.)

2. **Project File Paths**
   - Update all hardcoded paths in the code:
     - Face images folder
     - Haar cascade file path
     - Model save/load path

3. **Create Directory for Face Dataset**
   ```plaintext
   D:\UIT\First Year\Second sem\C++\Face Recognition Project\Faces\
   ```

4. **Ensure Haar Cascade File Exists**
   Example path:
   ```plaintext
   D:\UIT\First Year\Second sem\C++\C++ project 2\opencv\sources\data\haarcascades_cuda\
   ```

---

## ▶️ How to Use

### 1. Add Your Face

Prompts you for a name and captures 10 face images.

```cpp
addFace();
```

### 2. Train the Face Recognizer

Reads all images from the `Faces/` directory and trains an EigenFace model.

```cpp
eigenFaceTrainer();
```

### 3. Start Real-Time Recognition

Recognizes faces in webcam video stream using the trained model.

```cpp
FaceRecognition();
```

---

## 🧠 Technologies Used

- **Face Detection**: Haar Cascade (`haarcascade_frontalface_alt.xml`)
- **Face Recognition**: 
  - EigenFaceRecognizer
  - FisherFaceRecognizer
- **Preprocessing**: 
  - Grayscale conversion
  - Histogram equalization
  - Image resizing
- **OpenCV GUI**: `imshow()`, `waitKey()`, webcam feed

---

## 📌 Notes

- Images are stored with filenames based on user name and image count.
- Labels are inferred from filenames—consider using a proper database for scaling.
- Confidence scores are printed during recognition to evaluate certainty.

---

## 🧰 Future Improvements

- Use LBPH recognizer for better accuracy with real-world lighting
- Implement face alignment for better recognition
- Replace hardcoded paths with a config file
- Use a label-to-name mapping with a database or JSON file
- Add a cross-platform GUI

---

## 📷 Example Output

- Green rectangles around detected faces
- Label (user ID) shown above each recognized face
- Frame count and number of faces detected displayed

---

## 📬 Contact

For issues or contributions, feel free to open a pull request or reach out!
```

Let me know if you want me to extract and clean up the code into separate files, or create a version that uses dynamic paths instead of hardcoded Windows directories.

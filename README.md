# 🖼️ Image Processing with OpenCV

A comprehensive collection of introductory **Digital Image Processing** laboratory exercises developed using **Python**, **OpenCV**, and **NumPy**. This repository demonstrates fundamental image processing techniques such as grayscale conversion, thresholding, filtering, histogram processing, edge detection, segmentation, connected component analysis, face detection, and image transformations.

Designed for students and beginners, these practical exercises provide hands-on experience with OpenCV while strengthening core image processing concepts.

---

# 📚 Project Overview

This repository contains a series of laboratory exercises completed as part of a Digital Image Processing course. Each lab focuses on a specific image processing technique and includes well-documented Python scripts or Jupyter Notebooks for learning and experimentation.

---

# ✨ Features

* Image loading and display
* Grayscale image conversion
* Image thresholding techniques
* Image filtering and smoothing
* Image sharpening
* Histogram plotting and equalization
* Sobel, Laplacian, and Canny edge detection
* Hough Line Detection
* Image segmentation
* Connected Component Labeling
* Face detection using OpenCV
* Image rotation and saving
* Pixel manipulation using NumPy

---

# 🛠 Technologies Used

* Python 3.8+
* OpenCV
* NumPy
* Jupyter Notebook

---

# 📁 Project Structure

```text
Image_Processing/
│
├── Lab_1.py
├── Lab_2.py
├── lab3.ipynb
├── Lab4.ipynb
├── Lab7.ipynb
├── Lab10.ipynb
│
├── image_lab.png
├── image_lab.jpg
├── image_lab_gray.jpg        # Generated
├── image_lab_rotated.jpg     # Generated
├── segmented_output.png
├── component_output.png
├── video.mp4
│
└── README.md
```

---

# 📖 Laboratory Exercises

## 🔹 Lab 1 – Image Thresholding

**File:** `Lab_1.py`

### Objective

Explore various thresholding techniques provided by OpenCV.

### Topics Covered

* Image loading
* Thresholding
* Image visualization

### Threshold Types

* THRESH_BINARY
* THRESH_BINARY_INV
* THRESH_TRUNC
* THRESH_TOZERO
* THRESH_TOZERO_INV

### Input

```
image_lab.png
```

### Output

Displays:

* Original Image
* Binary Threshold
* Binary Inverted
* Truncated Image
* To-Zero Image
* To-Zero Inverted Image

### Run

```bash
python Lab_1.py
```

---

## 🔹 Lab 2 – Basic Image Operations

**File:** `Lab_2.py`

### Objective

Perform fundamental image processing operations using OpenCV and NumPy.

### Topics Covered

* Read image
* Convert RGB to Grayscale
* Display images
* Image dimensions
* Pixel access
* Rotate image (180°)
* Save processed images

### Input

```
image_lab.jpg
```

### Generated Output

```
image_lab_gray.jpg
image_lab_rotated.jpg
```

### Run

```bash
python Lab_2.py
```

---

## 🔹 Lab 3 – Image Filtering

**Notebook:** `lab3.ipynb`

### Topics Covered

* Average Filter
* Gaussian Filter
* Median Filter
* Bilateral Filter
* Kernel visualization
* Comparison of filtering techniques

---

## 🔹 Lab 4 – Histogram & Image Enhancement

**Notebook:** `Lab4.ipynb`

### Topics Covered

* Grayscale conversion
* Histogram plotting
* Histogram Equalization
* Image smoothing
* Image sharpening

---

## 🔹 Lab 7 – Image Segmentation

**Notebook:** `Lab7.ipynb`

### Topics Covered

* Image Segmentation
* Connected Component Labeling
* Face Detection
* Video Processing

### Input Files

* `image_lab.jpg`
* `video.mp4`

### Generated Files

* `segmented_output.png`
* `component_output.png`

---

## 🔹 Lab 10 – Edge Detection & Thresholding

**Notebook:** `Lab10.ipynb`

### Topics Covered

* Histogram Analysis
* Global Thresholding
* Adaptive Thresholding
* Otsu Thresholding
* Sobel Edge Detection
* Laplacian Edge Detection
* Canny Edge Detection
* Hough Line Detection

---

# ✅ Executed Notebooks

The following notebooks have been tested successfully.

| Notebook      | Status      | Description                                        |
| ------------- | ----------- | -------------------------------------------------- |
| `lab3.ipynb`  | ✅ Completed | Image filtering and kernel demonstrations          |
| `Lab4.ipynb`  | ✅ Completed | Histogram processing and enhancement               |
| `Lab7.ipynb`  | ✅ Completed | Segmentation, connected components, face detection |
| `Lab10.ipynb` | ✅ Completed | Thresholding and edge detection                    |

Run each notebook sequentially using **Jupyter Notebook** or **Visual Studio Code**.

---

# ⚙️ Requirements

* Python 3.8 or later
* OpenCV
* NumPy
* Jupyter Notebook (optional)

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/subhash107k/Image_Processing.git

cd Image_Processing
```

---

## Create a Virtual Environment (Recommended)

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install opencv-python numpy
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## Verify Installation

```bash
python -c "import cv2; print(cv2.__version__)"
python -c "import numpy; print(numpy.__version__)"
```

---

# ▶️ Running the Labs

```bash
python Lab_1.py
python Lab_2.py
```

For Jupyter notebooks:

```bash
jupyter notebook
```

Open the desired notebook and execute the cells sequentially.

---

# 🎯 Learning Outcomes

After completing these laboratory exercises, you will be able to:

* Understand digital image representation
* Read and display images using OpenCV
* Convert color images to grayscale
* Apply different thresholding methods
* Access and manipulate image pixels with NumPy
* Perform image transformations
* Apply smoothing and sharpening filters
* Analyze image histograms
* Detect edges using multiple techniques
* Perform image segmentation
* Detect faces using OpenCV
* Save processed images
* Build a strong foundation in Digital Image Processing

---

# 🚀 Future Improvements

* Replace hardcoded image paths with command-line arguments
* Support batch image processing
* Add image resizing and cropping
* Implement morphological operations
* Add contour detection
* Include color space transformations (HSV, LAB, YCrCb)
* Add feature detection (SIFT, SURF, ORB)
* Build a simple GUI using Tkinter or PyQt
* Add real-time webcam processing examples
* Improve documentation with sample output images

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve the repository:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your fork.
5. Open a Pull Request.

---

# 📄 License

This project is intended for educational purposes. You may freely use and modify the code for learning and academic projects.

---

# 👨‍💻 Author

**Subhash Sharma**

* GitHub: https://github.com/subhash107k
* Python • OpenCV • Computer Vision • Machine Learning • MERN Stack

If you find this repository useful, consider giving it a ⭐ on GitHub.

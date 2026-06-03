# Image Processing with OpenCV

A collection of introductory image processing laboratory exercises implemented using **Python**, **OpenCV**, and **NumPy**. These labs demonstrate fundamental image manipulation techniques, thresholding operations, grayscale conversion, image rotation, and file handling.

---

## Project Overview

This repository contains practical exercises designed to help students understand basic image processing concepts and gain hands-on experience with the OpenCV library.

### Technologies Used

* Python 3.x
* OpenCV
* NumPy

---

## Project Structure

```text
Image_Processing/
│
├── Lab_1.py
├── Lab_2.py
├── image_lab.png
├── image_lab.jpg
├── image_lab_gray.jpg      (generated)
├── image_lab_rotated.jpg   (generated)
└── README.md
```

---

## Requirements

* Python 3.8 or later
* OpenCV
* NumPy

Install the required dependencies:

```powershell
python -m pip install -r requirements.txt
```

### Verify Installation

```powershell
python -c "import cv2; print(cv2.__version__)"
python -c "import numpy; print(numpy.__version__)"
```

---

# Lab 1 – Image Thresholding

### File

```text
Lab_1.py
```

### Objective

Demonstrate various thresholding techniques available in OpenCV.

### Features

* Load and display an image
* Convert image intensity values using thresholding
* Compare different thresholding methods visually

### Thresholding Methods Demonstrated

* THRESH_BINARY
* THRESH_BINARY_INV
* THRESH_TRUNC
* THRESH_TOZERO
* THRESH_TOZERO_INV

### Input

* Reads an image specified inside the script (`image_lab.png`)

### Output

Displays:

* Original Image
* Binary Threshold Image
* Binary Inverted Image
* Truncated Image
* To-Zero Image
* To-Zero Inverted Image

### Run

```powershell
python Lab_1.py
```

---

# Lab 2 – Basic Image Operations

### File

```text
Lab_2.py
```

### Objective

Perform fundamental image processing operations using OpenCV and NumPy.

### Features

* Load image from the project directory
* Convert image to grayscale
* Display original and grayscale images
* Print image dimensions
* Access pixel data
* Rotate image by 180°
* Save processed images

### Input

```text
image_lab.jpg
```

### Output Files

```text
image_lab_gray.jpg
image_lab_rotated.jpg
```

### Run

```powershell
python Lab_2.py
```

---

## Setup Guide

### Create a Virtual Environment (Recommended)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
pip install opencv-python numpy
```

### Run the Labs

```powershell
python Lab_1.py
python Lab_2.py
```

---

## Learning Outcomes

After completing these labs, students will be able to:

* Understand digital image representation
* Load and display images using OpenCV
* Convert images to grayscale
* Apply image thresholding techniques
* Access image pixel data using NumPy
* Perform image transformations
* Save processed images
* Work with OpenCV image processing workflows

---

## Future Improvements

* Replace absolute image paths with relative paths
* Add command-line argument support
* Implement adaptive thresholding
* Add histogram visualization
* Add image resizing and cropping operations
* Support batch image processing
* Build a simple GUI for image selection

---

## Author

**Subhash Sharma**

GitHub: https://github.com/subhash107k

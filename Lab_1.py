import cv2
import os
import argparse

# ---------------- ARGUMENTS / IMAGE PATH ----------------
script_dir = os.path.dirname(os.path.abspath(__file__))
default_path = os.path.join(script_dir, 'image_lab.png')

parser = argparse.ArgumentParser(description='Lab 1: Demonstrate OpenCV thresholding')
parser.add_argument('image', nargs='?', default=default_path, help='Path to input image (default: image_lab.png in script dir)')
args = parser.parse_args()
path = args.image

# ---------------- LOAD IMAGE ----------------
img = cv2.imread(path, 0)

if img is None:
    print("Image not found! Check file path or name:", path)
    exit(1)

# ---------------- THRESHOLDING ----------------
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# ---------------- SHOW IMAGES ----------------
cv2.imshow("Original", img)
cv2.imshow("Binary", binary)
cv2.imshow("Binary Inv", binary_inv)
cv2.imshow("Trunc", trunc)
cv2.imshow("ToZero", tozero)
cv2.imshow("ToZero Inv", tozero_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Thresholding completed successfully")
import cv2
import os

# ---------------- IMAGE PATH ----------------
path = r"D:\My_Projects\College_Project\Image_Processing\image_lab.png"

# ---------------- LOAD IMAGE ----------------
img = cv2.imread(path, 0)

if img is None:
    print("❌ Image not found! Check file path or name.")
    exit()

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

print("✔ Thresholding completed successfully")
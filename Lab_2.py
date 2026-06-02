import os
import cv2
import numpy as np

# ---------------- LOAD IMAGE ----------------
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'image_lab.jpg')
image = cv2.imread(image_path)

print(f"Loading image from: {image_path}")
if image is None:
    print("❌ Image not found! Check file name/path")
    exit(1)

def show_image(title, img):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, img)
    cv2.waitKey(1)
    print(f"Showing '{title}'. Press any key in that window to continue.")
    cv2.waitKey(0)
    cv2.destroyWindow(title)

# ---------------- ORIGINAL IMAGE ----------------
show_image('Original Image', image)

# ---------------- GRAYSCALE ----------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
show_image('Grayscale Image', gray)

# ---------------- NUMPY ARRAY ----------------
data = np.asarray(image)
print("\nShape:", data.shape)
print("\nPixel Data:\n", data)

# ---------------- ROTATION ----------------
rotated = cv2.rotate(image, cv2.ROTATE_180)
show_image('Rotated Image (180°)', rotated)

# ---------------- SAVE OUTPUTS ----------------
gray_path = os.path.join(script_dir, 'image_lab_gray.jpg')
rotated_path = os.path.join(script_dir, 'image_lab_rotated.jpg')
cv2.imwrite(gray_path, gray)
cv2.imwrite(rotated_path, rotated)
print(f"Saved grayscale image to: {gray_path}")
print(f"Saved rotated image to: {rotated_path}")
print("✔ All images displayed successfully")
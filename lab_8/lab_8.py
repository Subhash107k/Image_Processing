import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from skimage.measure import label

# -----------------------------
# Read Image
# -----------------------------
img = cv2.imread("number_plate.jpg")

if img is None:
    raise FileNotFoundError("Could not read number_plate.jpg. Make sure it exists in the current folder.")

# Convert BGR to RGB (for display)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Median filtering
gray = cv2.medianBlur(gray, 3)

# -----------------------------
# Sobel Edge Detection
# -----------------------------
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

magnitude = np.sqrt(grad_x**2 + grad_y**2)

# Threshold (adjust if needed)
BW = (magnitude > 100).astype(np.uint8)

# -----------------------------
# Convolution Mask
# -----------------------------
mask = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
], dtype=np.uint8)

B = convolve2d(BW, mask, mode='same')

# -----------------------------
# Connected Component Labeling
# -----------------------------
L = label(B > 0, connectivity=2)

num_components = L.max()
print("Total Connected Components:", num_components)

# Extract Largest Component
component = np.zeros_like(BW, dtype=np.uint8)

if num_components > 0:
    sizes = np.bincount(L.ravel())
    sizes[0] = 0  # Ignore background
    largest_component = np.argmax(sizes)
    component[L == largest_component] = 255
    print("Largest Component:", largest_component)
else:
    print("No connected components found.")

# -----------------------------
# Save Output Images
# -----------------------------
cv2.imwrite("grayscale_output.png", gray)
cv2.imwrite("segmented_output.png", BW * 255)
cv2.imwrite("component_output.png", component)

print("Images saved successfully.")

# -----------------------------
# Display Images using Matplotlib
# -----------------------------
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(BW, cmap='gray')
plt.title("Segmented")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(component, cmap='gray')
plt.title("Largest Component")
plt.axis("off")

plt.tight_layout()
plt.show()

# -----------------------------
# Display Images using OpenCV
# (Optional)
# -----------------------------
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Segmented", BW * 255)
cv2.imshow("Largest Component", component)

print("Press any key on an image window to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()
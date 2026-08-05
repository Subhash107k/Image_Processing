import cv2
import os

# -----------------------------
# Load Haar Cascade Face Detector
# -----------------------------
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_detector.empty():
    print("Error: Could not load Haar Cascade classifier.")
    exit()


# -----------------------------
# Open Video File
# -----------------------------
video_path = "video.mp4"

if not os.path.exists(video_path):
    print(f"Error: '{video_path}' not found.")
    exit()

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: Could not open the video.")
    exit()


# -----------------------------
# Video Face Detection
# -----------------------------
total_faces = 0
frame_count = 0

while True:

    # Read frame
    ret, frame = video.read()

    if not ret:
        break


    frame_count += 1


    # -----------------------------
    # Convert Frame to Grayscale
    # -----------------------------
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    # -----------------------------
    # Detect Faces
    # -----------------------------
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )


    # Update face count
    total_faces = len(faces)


    # -----------------------------
    # Draw Rectangle Around Faces
    # -----------------------------
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )


        cv2.putText(
            frame,
            "Face",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )


    # -----------------------------
    # Display Face Count
    # -----------------------------
    cv2.putText(
        frame,
        f"Faces Detected: {total_faces}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )


    # -----------------------------
    # Show Video Output
    # -----------------------------
    cv2.imshow(
        "Haar Cascade Face Detection",
        frame
    )


    # Press Q to exit
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break



# -----------------------------
# Release Resources
# -----------------------------
video.release()
cv2.destroyAllWindows()


print("Video Processing Completed")
print("Total Frames Processed:", frame_count)
print("Last Frame Faces Detected:", total_faces)
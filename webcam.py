from ultralytics import YOLO
import cv2
import torch

# Load YOLO model
model = YOLO("yolo11n.pt")

# Use GPU if available
device = 0 if torch.cuda.is_available() else "cpu"

print("Using device:", "GPU" if device == 0 else "CPU")

# Open webcam
cap = cv2.VideoCapture(0)

# Reduce camera buffering for lower delay
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read camera")
        break

    # Faster YOLO inference
    results = model(
        frame,
        conf=0.40,
        imgsz=320,
        device=device,
        verbose=False
    )

    # Draw detections
    annotated_frame = results[0].plot()

    cv2.imshow("AI Object Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
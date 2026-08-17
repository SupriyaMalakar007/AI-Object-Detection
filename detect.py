from ultralytics import YOLO
from pathlib import Path

model = YOLO("yolo11n.pt")

image_folder = Path("dataset/images")

for image in image_folder.glob("*.*"):
    print(f"\nProcessing: {image.name}")

    results = model(image)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            name = result.names[class_id]

            print(f"Object: {name}")
            print(f"Confidence: {confidence:.2f}")
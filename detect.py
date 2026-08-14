from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("test.jpg")

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        name = result.names[class_id]

        print("Object:", name)
        print("Confidence:", confidence)
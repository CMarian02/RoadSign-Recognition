from ultralytics import YOLO

# Încarcă modelul pre-antrenat YOLOv8
model = YOLO("C:/Users/CMarian/Desktop/Road Sign Recogniton/runs/detect/train/weights/best.pt")  # poți folosi și 'yolov8s.pt', 'yolov8m.pt' etc., în funcție de dimensiunea modelului

# Antrenează modelul pe datasetul tău personalizat
# model.train(data="C:/Users/CMarian/Desktop/test/YOLODataset/dataset.yaml", epochs=50)

model.predict("53.png")
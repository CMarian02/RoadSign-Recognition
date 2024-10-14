from ultralytics import YOLO

model = YOLO('yolo11l.pt') 

# model.train(data="config.yaml", epochs=80, resume=True)

# results = model.predict("C:/Users/CMarian/Desktop/PP/RoadSign-Recognition/dataset/all-signs/images/Zona_cu_viteza_limitata_la_30_kmh.png", save=True, show=True)


# Afișează rezultatele
# print(results)
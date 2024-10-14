from PIL import Image
import os

input_folder = 'C:/Users/CMarian/Desktop/PP/RoadSign-Recognition/dataset/trecere-pietoni' 
output_folder = 'C:/Users/CMarian/Desktop/PP/RoadSign-Recognition/test_img' 

target_size = (640, 640)


for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')): 
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
            img_resized.save(os.path.join(output_folder, filename))

print(f"Imaginile au fost redimensionate și salvate în {output_folder}")

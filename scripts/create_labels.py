import os

images_folder = 'dataset/images'  
labels_folder = 'dataset/labels'  




for filename in os.listdir(images_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  

        file_name_without_ext = os.path.splitext(filename)[0]

        label_file_path = os.path.join(labels_folder, file_name_without_ext + '.txt')
        
        with open(label_file_path, 'w', encoding='utf-8') as f:
            f.write('')
        
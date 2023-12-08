import os

def find_images(directory):
    file_paths = []
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico']
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in image_extensions):
                path = directory + '/' + f'{file}'
                file_paths.append(path)
                

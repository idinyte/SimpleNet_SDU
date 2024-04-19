import os
from PIL import Image

for root, dirs, files in os.walk("."):
    for file in files:
        if ".png" in file:
            file_path = os.path.join(root, file)
            image = Image.open(file_path)
            width, height = image.size
            crop_size = (min(image.size), min(image.size))
            left = (width - crop_size[0]) / 2
            top = (height - crop_size[1]) / 2
            right = (width + crop_size[0]) / 2
            bottom = (height + crop_size[1]) / 2
            cropped_image = image.crop((left, top, right, bottom))
            cropped_image.save(file_path)
            
            #print(file_path)
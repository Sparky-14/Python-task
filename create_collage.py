# <------TASK 3------->
# <------COLLAGE IMG------->

from PIL import Image
import os

def validate_image_paths(image_paths):
    """
    Validate that all provided paths exist and point to valid image files.
    """
    for path in image_paths:
        if not os.path.isfile(path):
            return "File not found: {}".format(path)
        try:
            with Image.open(path) as img:
                img.verify()  
        except Exception as e:
            return "Invalid image file at {}: {}".format(path, e)
    return None

def resize_images(images, target_size):
    """
    Resize all images to the target size (width, height).
    """
    resized = [img.resize(target_size, Image.Resampling.LANCZOS) for img in images]
    return resized

def create_collage(image_paths, output_file="collage.jpg"):
    """
    Create a 2x2 collage from the given image paths and save it to the output file.
    """
    
    error = validate_image_paths(image_paths)
    if error:
        print(error)
        return

    
    images = [Image.open(path) for path in image_paths]

    
    min_width = min(img.width for img in images)
    min_height = min(img.height for img in images)
    resized_images = resize_images(images, (min_width, min_height))

    
    collage_width = min_width * 2
    collage_height = min_height * 2
    collage = Image.new("RGB", (collage_width, collage_height))

    
    collage.paste(resized_images[0], (0, 0))
    collage.paste(resized_images[1], (min_width, 0))
    collage.paste(resized_images[2], (0, min_height))
    collage.paste(resized_images[3], (min_width, min_height))

    
    collage.save(output_file, format="JPEG")
    print("Collage saved as {}".format(output_file))

if __name__ == "__main__":
    
    print("Enter paths to 4 images:")
    image_paths = [input("Path to image {}: ".format(i + 1)).strip() for i in range(4)]

    
    output_file = "collage.jpg"

    
    create_collage(image_paths, output_file)



from PIL import Image
import os

def resize_image(image_path, output_path, size=(150, 150)):
    """Resize the image to the given size while maintaining the aspect ratio."""
    try:
        with Image.open(image_path) as img:
            # Resize with aspect ratio maintained
            img.thumbnail(size)
            img.save(output_path)
            print(f"Thumbnail saved to {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def resize_images_in_current_folder(size=(150, 150)):
    """Resize all images in the current folder to thumbnails."""
    current_folder = os.getcwd()  # Get the current working directory
    
    # Create a folder for thumbnails if it doesn't exist
    thumbnails_folder = os.path.join(current_folder, 'thumbnails')
    if not os.path.exists(thumbnails_folder):
        os.makedirs(thumbnails_folder)

    # Loop through all files in the current folder
    for filename in os.listdir(current_folder):
        file_path = os.path.join(current_folder, filename)
        
        # Check if it's a valid image file (you can expand this list as needed)
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            output_path = os.path.join(thumbnails_folder, filename)
            resize_image(file_path, output_path, size)

if __name__ == "__main__":
    resize_images_in_current_folder(size=(150, 150))
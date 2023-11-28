from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    with Image.open(input_path) as img:
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_path)
        print(f"Image saved successfully at {output_path}")


input_image_path = 'IMG_FC925768CC8B-1.jpeg'  # Replace with your image path

# iOS 5.5 specifications
iOS_5_5_width = 1242
iOS_5_5_height = 2208

resize_image(input_image_path, "iOS_5_5.jpg", iOS_5_5_width, iOS_5_5_height)

# iOS 6.5 specifications
iOS_6_5_width = 1242
iOS_6_5_height = 2688

resize_image(input_image_path, "iOS_6_5.jpg", iOS_6_5_width, iOS_6_5_height)

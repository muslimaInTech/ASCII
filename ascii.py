import numpy as np
import PIL.Image

# Define the ASCII characters to be used
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Resize the image to fit the screen
def resize_image(image, new_width=100):
    width, height = image.size
    new_height = int(new_width * height / width)
    return image.resize((new_width, new_height))

# Convert each pixel to an ASCII character
def pixel_to_ascii(pixel):
    # Scale the pixel's brightness to the range [0, 9]
    brightness = int(sum(pixel) / 3 / 256 * 10)
    return ASCII_CHARS[brightness]

# Convert the image to ASCII art
def image_to_ascii(image):
    image = resize_image(image)
    pixels = np.array(image.convert('RGB'))
    ascii_art = ""
    for row in pixels:
        ascii_row = ""
        for pixel in row:
            ascii_row += pixel_to_ascii(pixel)
        ascii_art += ascii_row + "\n"
    return ascii_art

# Example usage
image = PIL.Image.open("car.jpeg")
ascii_art = image_to_ascii(image)
print(ascii_art)

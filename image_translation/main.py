import cv2
import sys
from to_ascii import ASCIIConverter
from to_img import ImageConverter
from app_api import AppAPI


def main():
    path = input("Enter the path to the image:\n")

    try:
        with open(path, 'rb'):
            pass
    except FileNotFoundError:
        print("Error: The specified image file does not exist.")
        sys.exit(1)

    img = cv2.imread(path)

    converter_ascii = ASCIIConverter()
    converter_image = ImageConverter(path)

    image_text = converter_image.convert_image()
    ascii_text = converter_ascii.convert_img_to_ascii(img)
    api = AppAPI(ascii_text, image_text, img)
    api.run()


if __name__ == "__main__":
    main()

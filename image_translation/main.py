import cv2
from to_ascii import ASCIIConverter
from app_api import AppAPI


def main():
    converter = ASCIIConverter()

    path = input("Введите путь до изображения\n")
    img = cv2.imread(path)

    ascii_text = converter.convert_img_to_ascii(img)

    api = AppAPI(ascii_text, img)
    api.run()


if __name__ == "__main__":
    main()

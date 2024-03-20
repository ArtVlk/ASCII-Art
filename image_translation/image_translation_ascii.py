import os
import PIL.Image

# От темного к светлому, всего 11,
# больше лучше не надо, так как менее понятная картинка становится
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=100):
    width, height = image.size
    relationship_width_and_height = height / width
    new_height = int(new_width * relationship_width_and_height)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def converting_image_to_gray(image):
    # изображение в палитру серых оттенков
    gray_image = image.convert("L")
    return gray_image


def convert_pixels_to_ascii(image):
    # Получение значений пикселей
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(new_width=100):
    path = input("Введите путь до изображения\n")
    try:
        image = PIL.Image.open(path)
    except FileNotFoundError:
        print(path, " Этот путь к файлу неверен")
        return

    new_image = convert_pixels_to_ascii(
        converting_image_to_gray(resize_image(image)))

    pixel_count = len(new_image)
    ascii_image = "\n".join([new_image[index:(index + new_width)]
                             for index in range(0, pixel_count, new_width)])

    print(ascii_image)

    file_name = os.path.basename(path)
    # путь к папке из родительской директории
    directory = os.path.join("..", "art")

    if not os.path.exists(directory):
        os.makedirs(directory)

    art_path = os.path.join(directory, file_name + "_ascii.txt")

    with open(art_path, "w") as f:
        f.write(ascii_image)


if __name__ == "__main__":
    main()

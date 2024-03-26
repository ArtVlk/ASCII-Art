import os
import PIL.Image
<<<<<<< HEAD
import tkinter as tk

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
CHAR_WIDTH = 6
CHAR_HEIGHT = 10
MAX_HEIGHT = 65
MAX_WIDTH = 200


def resize_image(image, size):
    width, height = image.size
    if not size:
        ratio = max(height, width) / min(height, width)
        new_height = min(height, int(MAX_HEIGHT * ratio))
        new_width = min(width, int(MAX_WIDTH * ratio))
        resized_image = image.resize((new_width, new_height))
    else:
        new_width = size[1]
        resized_image = image.resize((new_width, size[0]))
    return resized_image, new_width


def convert_image_to_gray(image):
=======

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
>>>>>>> origin/main
    gray_image = image.convert("L")
    return gray_image


def convert_pixels_to_ascii(image):
<<<<<<< HEAD
=======
    # Получение значений пикселей
>>>>>>> origin/main
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


<<<<<<< HEAD
def file_path_save(path):
    file_name = os.path.basename(path)
    directory = os.path.join("..", "art")
=======
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

>>>>>>> origin/main
    if not os.path.exists(directory):
        os.makedirs(directory)

    art_path = os.path.join(directory, file_name + "_ascii.txt")

<<<<<<< HEAD
    return art_path


def display_ascii_image(ascii_image, path):
    lines = ascii_image.split('\n')
    width = len(lines[0]) * CHAR_WIDTH
    height = len(lines) * CHAR_HEIGHT

    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    y = 0
    for line in lines:
        x = 0
        for char in line:
            canvas.create_text(x, y, text=char, anchor='nw')
            x += CHAR_WIDTH
        y += CHAR_HEIGHT

    save_button = tk.Button(root, text="Сохранить", command=lambda: save_ascii_image(ascii_image, file_path_save(path)))
    save_button.pack(side=tk.LEFT)

    cancel_button = tk.Button(root, text="Отменить", command=root.destroy)
    cancel_button.pack(side=tk.RIGHT)

    root.mainloop()


def save_ascii_image(image, file_path):
    with open(file_path, "w") as f:
        f.write(image)


def main():
    path = input("Введите путь до изображения\n")

    try:
        image = PIL.Image.open(path)
    except FileNotFoundError:
        print(path, "Этот путь к файлу неверен")
        return
    try:
        size = list(map(int, input("Введите, если нужно, сначала высоту, потом ширину, иначе оставьте пустым\n").split()))
    except ValueError:
        print("Нельзя привести к int")
        return
    new_image, new_width = resize_image(image, size)
    new_gray_image = convert_pixels_to_ascii(
        convert_image_to_gray(new_image))

    pixel_count = len(new_gray_image)
    ascii_image = "\n".join([new_gray_image[index:(index + new_width)]
                             for index in range(0, pixel_count, new_width)])

    display_ascii_image(ascii_image, path)
=======
    with open(art_path, "w") as f:
        f.write(ascii_image)
>>>>>>> origin/main


if __name__ == "__main__":
    main()

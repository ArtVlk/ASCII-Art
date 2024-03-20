import os
import PIL.Image
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
    gray_image = image.convert("L")
    return gray_image


def convert_pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def file_path_save(path):
    file_name = os.path.basename(path)
    directory = os.path.join("..", "art")
    if not os.path.exists(directory):
        os.makedirs(directory)

    art_path = os.path.join(directory, file_name + "_ascii.txt")

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


if __name__ == "__main__":
    main()

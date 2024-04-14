import cv2
import tkinter as tk
from tkinter import messagebox, filedialog

import numpy
from PIL import Image, ImageTk


class AppAPI:
    def __init__(self, ascii_text, image_text, img):
        self.root = tk.Tk()
        self.ascii_text = ascii_text
        self.image_text = image_text
        self.img = img
        self.root.resizable(False, False)

    def display_ascii(self):
        ascii_window = tk.Toplevel(self.root)
        ascii_window.title("ASCII Art")
        ascii_label = tk.Label(ascii_window,
                               text=self.ascii_text,
                               font=("Courier", 8))
        ascii_label.pack()

    def display_ascii_image(self):
        ascii_image_window = tk.Toplevel(self.root)
        ascii_image_window.title("Colored ASCII")

        img_tk = ImageTk.PhotoImage(self.image_text)
        label = tk.Label(ascii_image_window, image=img_tk)
        label.image = img_tk
        label.pack()

    def save_image(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )
        if file_path:
            img_rgb = cv2.cvtColor(numpy
                                   .array(self.image_text),
                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite(file_path, img_rgb)
            messagebox.showinfo("Saved", f"Image saved to {file_path}")

    def save_ascii(self):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")]
            )
            if file_path:
                with open(file_path, 'w') as f:
                    f.write(self.ascii_text)
                messagebox.showinfo("Saved",
                                    "ASCII art saved to {}".format(file_path))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def on_exit(self):
        self.root.destroy()

    def run(self):
        img = Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        img.thumbnail((800, 800))
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(self.root, image=img_tk)
        label.image = img_tk
        label.pack()

        f_top = tk.Frame(self.root)
        f_bot = tk.Frame(self.root)

        display_ascii_button = tk.Button(f_top,
                                         text="Display ASCII",
                                         command=self.display_ascii,
                                         bg="lightblue",
                                         width=15)
        display_ascii_button.pack(side=tk.LEFT)

        display_ascii_image_button = tk.Button(f_top,
                                               text="Display Image",
                                               command=self.
                                               display_ascii_image,
                                               bg="lightblue",
                                               width=15)
        display_ascii_image_button.pack(side=tk.RIGHT)

        save_ascii_button = tk.Button(f_bot,
                                      text="Save ASCII",
                                      command=self.save_ascii,
                                      bg="lightblue",
                                      width=15)
        save_ascii_button.pack(side=tk.LEFT)

        save_button = tk.Button(f_bot, text="Save Image",
                                command=self.save_image,
                                bg="lightblue",
                                width=15)
        save_button.pack(side=tk.RIGHT)

        f_top.pack()
        f_bot.pack()

        exit_button = tk.Button(self.root,
                                text="Exit",
                                command=self.on_exit,
                                bg="lightblue",
                                width=15)
        exit_button.place(relx=1.0,
                          rely=1.0,
                          anchor='se')

        self.root.mainloop()

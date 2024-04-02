import cv2
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


class AppAPI:
    def __init__(self, ascii_text, img):
        self.root = tk.Tk()
        self.ascii_text = ascii_text
        self.img = img

    def display_ascii(self):
        ascii_window = tk.Toplevel(self.root)
        ascii_window.title("ASCII Art")
        ascii_label = tk.Label(ascii_window,
                               text=self.ascii_text,
                               font=("Courier", 8))
        ascii_label.pack()

    def save_image(self):
        file_path = (filedialog
                     .asksaveasfilename
                     (defaultextension=".png",
                      filetypes=[("PNG files", "*.png")]))
        if file_path:
            cv2.imwrite(file_path, self.img)
            messagebox.showinfo("Saved", "Image sav ed to {}"
                                .format(file_path))

    def save_ascii(self):
        file_path = (filedialog
                     .asksaveasfilename
                     (defaultextension=".txt",
                      filetypes=[("Text files", "*.txt")]))
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.ascii_text)
            messagebox.showinfo("Saved", "ASCII art saved to {}"
                                .format(file_path))

    def on_exit(self):
        self.root.destroy()

    def run(self):
        img = Image.fromarray(cv2.cvtColor(self.img, cv2
                                           .COLOR_BGR2RGB))
        img.thumbnail((800, 800))
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(self.root, image=img_tk)
        label.image = img_tk
        label.pack()

        save_button = tk.Button(self.root, text="Save Image",
                                command=self.save_image)
        save_button.pack()

        save_ascii_button = tk.Button(self.root, text="Save ASCII",
                                      command=self.save_ascii)
        save_ascii_button.pack()

        display_ascii_button = tk.Button(self.root, text="Display ASCII",
                                         command=self.display_ascii)
        display_ascii_button.pack()

        exit_button = tk.Button(self.root, text="Exit",
                                command=self.on_exit)
        exit_button.pack()

        self.root.mainloop()

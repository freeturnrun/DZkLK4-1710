import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Приветствие")
        self.root.geometry("600x640+100+100")
        self.setup_main_window()

    def setup_main_window(self):
        image_path = "bmw.jpg"
        try:
            if os.path.exists(image_path):
                self.bg_image = Image.open(image_path)
                self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((600, 640), Image.Resampling.LANCZOS))

                bg_label = tk.Label(self.root, image=self.bg_photo)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                bg_label.lower()
            else:
                print(f"Файл {image_path} не найден")
                self.root.configure(bg='black')
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            self.root.configure(bg='black')

        hello_label = tk.Label(
            self.root,
            text="Здравствуйте!",
            font=("Calibri", 60, "bold"),
            fg="black",
            bg="white"
        )
        hello_label.place(x=50, y=300)


class MainWindow1:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Резюме")
        self.root.geometry("500x800+100+100")
        self.setup_main_window()

    def create_image_labels(self):
        bg_image = "back.jpg"
        try:
            if os.path.exists(bg_image):
                self.bg_image = Image.open(bg_image)
                self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((500, 800), Image.Resampling.LANCZOS))

                self.bg_label = tk.Label(self.root, image=self.bg_photo)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                self.bg_label.lower()
            else:
                print(f"Не удалось загрузить {bg_image}")
                self.root.configure(bg='black')
        except Exception as e:
            print(f"Ошибка загрузки фонового изображения: {e}")
            self.root.configure(bg='black')


        fg_image = "photo.jpg"
        if fg_image and os.path.exists(fg_image):
            try:
                self.fg_image = Image.open(fg_image)
                self.fg_image.thumbnail((300, 200), Image.Resampling.LANCZOS)
                self.fg_photo = ImageTk.PhotoImage(self.fg_image)

                fg_label = tk.Label(self.root, image=self.fg_photo)
                fg_label.place(x=170, y=60)
            except Exception as e:
                print(f"Ошибка загрузки переднего изображения: {e}")

    def setup_main_window(self):
        self.create_image_labels()

        user_label = tk.Label(
            self.root,
            text="Борзаев Баир",
            font=("Calibri", 32),
            fg="black",
            bg="white"
        )
        user_label.place(x=83, y=0)


        bio_label = tk.Label(
            self.root,
            text="Биография:",
            font=("Calibri", 25),
            fg="black",
            bg="white"
        )
        bio_label.place(x=10, y=260)

        about_label = tk.Label(
            self.root,
            text="г.Элиста, 20.09.2006",
            font=("Calibri", 18),
            fg="black",
            bg="white",
            wraplength=300
        )
        about_label.place(x=190, y=260)

        skills_label = tk.Label(
            self.root,
            text="Умения:",
            font=("Calibri", 25),
            fg="black",
            bg="white"
        )
        skills_label.place(x=10, y=350)

        languages_label = tk.Label(
            self.root,
            text="стиль",
            font=("Calibri", 18),
            fg="black",
            bg="white"
        )
        languages_label.place(x=135, y=357)


        experience_label = tk.Label(
            self.root,
            text="Опыт:",
            font=("Calibri", 25),
            fg="black",
            bg="white"
        )
        experience_label.place(x=10, y=400)

        developer_label = tk.Label(
            self.root,
            text="озон",
            font=("Calibri", 18),
            fg="black",
            bg="white"
        )
        developer_label.place(x=105, y=407)


def main():
    window = MainWindow()

    window1 = MainWindow1()

    window.root.mainloop()


if __name__ == '__main__':
    main()
import tkinter as tk
from tkinter import filedialog
from src.ImageReader import RawDataSetter, ImageVisualizer

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    d = RawDataSetter(file_path, size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    d.read_files()

    v = ImageVisualizer(d)
    v.sum_image()
    v.max_image()

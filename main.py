import os
import tkinter as tk
from tkinter import filedialog
from src.ImageReader import RawDataSetter, ImageVisualizer
from src.ExcelReader import SuvReader, SuvDisplayer

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    # file_path = filedialog.askopenfilename()

    # d = RawDataSetter(file_path, size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    # d.read_files()
    #
    # v = ImageVisualizer(d)
    # v.sum_image()
    # v.max_image()
    # v.organ(13)

    excel_file_name = "SUV values backup.xlsx"
    main_dir = os.path.dirname(os.path.abspath(__file__))  # directory of main file
    excel_file_path = os.path.join(main_dir, "bin", excel_file_name)  # directory of excel file

    data = SuvReader(excel_file_path)
    data.read_file()

    grapher = SuvDisplayer(data)
    grapher.graphic()


import os
import tkinter as tk
from tkinter import filedialog
from src.ImageReader import RawDataSetter, ImageVisualizer
from src.ExcelReader import SuvReader, SuvDisplayer
from src.Atlas import Atlas

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    data_setter = RawDataSetter(file_path, size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    data_setter.read_files()

    # Atlas
    main_dir = os.path.dirname(os.path.abspath(__file__))  # directory of main file
    atlas_file_name = "atlas.txt"
    atlas_file_path = os.path.join(main_dir, "bin")

    atlas = Atlas(atlas_file_path, atlas_file_name)
    atlas.load_file()

    visualizer = ImageVisualizer(data_setter)
    ax = 1
    visualizer.sum_image(ax)
    visualizer.max_image(ax)
    visualizer.organ(atlas.atlas_data["kidney_activity"], ax)

    # Excel
    # excel_file_name = "SUV_values_backup.xlsx"
    # excel_file_path = os.path.join(main_dir, "bin", excel_file_name)  # directory of excel file
    #
    # suv_data = SuvReader(excel_file_path)
    # suv_data.read_file()
    #
    # grapher = SuvDisplayer(suv_data)
    # grapher.graphic_organ()
    # grapher.graphic_mean()

import os
import tkinter as tk
import matplotlib.pyplot as plt
from src.ImageReader import RawDataSetter, ImageVisualizer
from src.ExcelReader import SuvReader, SuvDisplayer
from src.Segmentation import GroundTruth, Segmentation, RegionInterest, MiceData
from src.Metrics import Metrics

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    main_dir = os.path.dirname(os.path.abspath(__file__))  # directory of main file

    # --- Atlas ---
    atlas_image_file_name = "Moby_average_act_av.bin"
    atlas_image_file_path = os.path.join(main_dir, "bin")

    data_setter_atlas = RawDataSetter(file_name=os.path.join(atlas_image_file_path, atlas_image_file_name),
                                      size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    data_setter_atlas.read_files()
    atlas_volume = data_setter_atlas.volume

    # --- Excel ---
    # human_excel_file_name = "SUV_values_backup.xlsx"
    # human_excel_file_path = os.path.join(main_dir, "bin", human_excel_file_name)  # directory of excel file

    mice_excel_file_name = "SUV_mice.xlsx"
    mice_excel_file_path = os.path.join(main_dir, "bin", mice_excel_file_name)  # directory of excel file

    suv_data = SuvReader(mice_excel_file_path)
    suv_data.read_file()
    mice_dict = suv_data.mice_dict

    # grapher = SuvDisplayer(suv_data)
    # grapher.read_file()

    # --- Activity file ---
    act_file_name = "activity_map_generated.dat"
    act_file_path = os.path.join(main_dir, "bin")

    data_setter_act = RawDataSetter(file_name=os.path.join(act_file_path, act_file_name),
                                    size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    data_setter_act.read_files()
    activity_volume = data_setter_act.volume

    # --- Data of Activity ---
    voxel_volume = (0.145 * 0.145 * 0.145) * 0.001  # cm^3 -> mL
    activity_injected = 18500000
    temp = MiceData(mice_dict, activity_volume, atlas_volume, voxel_volume, activity_injected)
    temp.get_activity_organs()
    mice_dict = temp.mice_dict
    activity_all_organs = temp.activity_all_organs
    volume_all_organs = temp.volume_all_organs

    # --- Ground Truth ---
    organs_of_interest = ["Hippocampus"]
    temp = GroundTruth(activity_volume, atlas_volume, mice_dict)
    temp.get_ground_truth(organs_of_interest)

    ground_truth = temp.act_data
    mask_ground_truth = temp.roi

    # --- Segmentation ---
    temp = Segmentation(mice_dict, activity_volume)
    # temp.marching_cubes()
    # temp.k_means()
    temp.bayesian_gaussian()
    segmentation_volume = temp.segmentation

    # --- Region of Interest ---
    temp = RegionInterest(activity_volume, segmentation_volume, mask_ground_truth)
    # temp.region_to_segment()
    segmented_image = temp.segmented_image

    # --- Metrics ---
    temp = Metrics(ground_truth, ground_truth)
    # temp.get_metrics()
    # print("SNR:", temp.SNR)
    # print("NRMSE:", temp.NRMSE)

    # --- Visualization ---
    ax = 1
    plt.figure()
    plt.title("Ground Truth")
    visualizer = ImageVisualizer(ground_truth)
    # visualizer.sum_image(ax)
    visualizer.max_image(ax)
    #
    # plt.figure()
    # plt.title("Activity Data")
    # visualizer = ImageVisualizer(activity_volume)
    # visualizer.max_image(1)
    #
    # plt.figure()
    # plt.title("Segmentation by K-Means method (All organs)")
    # visualizer = ImageVisualizer(segmentation_volume)
    # visualizer.max_image(ax)
    #
    # plt.figure()
    # plt.title("Segmentation by K-Means method (Region of interest)")
    # visualizer = ImageVisualizer(segmented_image)
    # visualizer.max_image(ax)

    # --- Write files to visualize in AMIDE ---
    # r = RawDataSetter(file_name=os.path.join(main_dir, "bin", "bayesian_16_full.dat"), volume=segmentation_volume)
    # r.write_files_simple_binary()
    plt.show()

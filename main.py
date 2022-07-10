import os
import tkinter as tk
import matplotlib.pyplot as plt
from src.ImageReader import RawDataSetter, ImageVisualizer
from src.ExcelReader import SuvReader, SuvDisplayer
from src.Segmentation import GroundTruth, Segmentation, RegionInterest, MiceData
from src.Metrics import Metrics
import numpy as np

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    main_dir = os.path.dirname(os.path.abspath(__file__))  # directory of main file

    # # --- Atlas ---
    # atlas_image_file_name = "Moby_average_act_av.bin"
    # atlas_image_file_path = os.path.join(main_dir, "bin")
    #
    # data_setter_atlas = RawDataSetter(file_name=os.path.join(atlas_image_file_path, atlas_image_file_name),
    #                                   size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    # data_setter_atlas.read_files()
    # atlas_volume = data_setter_atlas.volume

    # # --- Excel ---
    # mice_excel_file_name = "SUV_mice.xlsx"
    # mice_excel_file_path = os.path.join(main_dir, "bin", mice_excel_file_name)  # directory of excel file
    #
    # suv_data = SuvReader(mice_excel_file_path)
    # suv_data.read_mice()
    # mice_dict = suv_data.mice_dict

    # --- Activity file ---
    # act_file_name = "activity_map_generated.dat"
    # act_file_path = os.path.join(main_dir, "bin")
    #
    # data_setter_act = RawDataSetter(file_name=os.path.join(act_file_path, act_file_name),
    #                                 size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    # data_setter_act.read_files()
    # activity_volume = data_setter_act.volume

    # --- Data of Activity ---
    # voxel_volume = (0.145 * 0.145 * 0.145) * 0.001  # cm^3 -> mL
    # activity_injected = 18500000
    # temp = MiceData(mice_dict, activity_volume, atlas_volume, voxel_volume, activity_injected)
    # temp.get_activity_organs()
    # mice_dict = temp.mice_dict
    # activity_all_organs = temp.activity_all_organs
    # normalized_activity_all_organs = temp.normalized_activity_all_organs
    # volume_all_organs = temp.volume_all_organs

    # --- Ground Truth ---
    # organs_of_interest = ["Hippocampus"]
    #[organ for organ in mice_dict.keys() if mice_dict[organ]["id"] != "None" and organ != "Anterior commissure" and organ != "Brain stem"]

    # for organ in organs_of_interest:

        # temp = GroundTruth(activity_volume, atlas_volume, mice_dict)
        # temp.get_ground_truth([organ])
        # ground_truth = temp.ground_truth
        # mask_ground_truth = temp.roi

    # --- Segmentation ---
    #     temp = Segmentation(mice_dict, activity_volume, normalized_activity_all_organs)
    #     # temp.k_means()
    #     # temp.gaussian()
    #     temp.bayesian_gaussian()
    #     segmentation_volume = temp.segmentation

    # --- Region of Interest ---
    #     temp = RegionInterest(activity_volume, segmentation_volume, mask_ground_truth, activity_all_organs)
    #     temp.bayesian_calculate_roi()
    #     segmented = temp.segmented_image

        # plt.figure()
        # plt.imshow(np.max(segmented[:, :, :], axis=1))
        # plt.title("Organ: " + organ)
        # plt.show()
    #
    # # --- Metrics ---
    # # truth_file_name = "ground_truth_fimbria"
    # # truth_file_path = os.path.join(main_dir, "bin")
    # #
    # # data_setter_atlas = RawDataSetter(file_name=os.path.join(truth_file_path, truth_file_name),
    # #                                   size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    # # data_setter_atlas.read_files()
    # # ground_truth = data_setter_atlas.volume
    # #
    # # image_file_name = "bayesian_16_diag_fimbria"
    # # image_file_path = os.path.join(main_dir, "bin")
    # #
    # # data_setter_atlas = RawDataSetter(file_name=os.path.join(image_file_path, image_file_name),
    # #                                   size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    # # data_setter_atlas.read_files()
    # # segmented = data_setter_atlas.volume
    # #

        # temp = Metrics(ground_truth, segmented)
        # temp.get_metrics()
        # temp.get_mae()
        # temp.calculate_psnr()
        # print("Organ:", organ)
        # print("SNR:", temp.SNR)
        # print("MSE:", temp.MSE)
        # print("MAE:", temp.MAE)
        # print("Other SNR:", temp.test)
        # print("Other SNR 2:", temp.test2)
        # print("mse:", temp.mse)
        # print("volume:", temp.volume)

    # # --- Visualization ---
    # # ax = 1
    # # plt.figure()
    # # # plt.title("Ground Truth")
    # # visualizer = ImageVisualizer(segmentation_volume)
    # # # visualizer.sum_image(ax)
    # # visualizer.max_image(ax)
    # # plt.show()
    #
    # # --- Write files to visualize in AMIDE ---
    # # r = RawDataSetter(file_name=os.path.join(main_dir, "bin", "K_means"), volume=segmentation_volume)
    # # r.write_files_simple_binary()
    #
        # r = RawDataSetter(file_name=os.path.join(main_dir, "results", "bayesian_16_diag_hippocampus.dat"), volume=segmented)
        # r.write_files_simple_binary()


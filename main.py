import os
import tkinter as tk
import matplotlib.pyplot as plt
from src.ImageReader import RawDataSetter
from src.ExcelReader import SuvReader
from src.ImageReader.imagevisualization import ImageVisualizer
from src.Segmentation import GroundTruth, Segmentation, RegionInterest, MiceData
from src.Metrics import Metrics
import numpy as np

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))


def retrieve_atlas_data():
    """Read data from the MOBY phantom"""
    atlas_image_file_name = "Moby_average_act_av.bin"
    atlas_image_file_path = os.path.join(MAIN_DIR, "bin")

    data_setter_atlas = RawDataSetter(file_name=os.path.join(atlas_image_file_path, atlas_image_file_name), size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    data_setter_atlas.read_files()
    return data_setter_atlas.volume


def retrieve_mice_data():
    """Read data from mice activity and parse it into dictionary"""
    mice_excel_file_name = "SUV_mice.xlsx"
    mice_excel_file_path = os.path.join(MAIN_DIR, "bin", mice_excel_file_name)

    suv_data = SuvReader(mice_excel_file_path)
    return suv_data.read_mice()
    

def retrieve_activity_data():
    """Read data from activity map"""
    act_file_name = "activity_map_generated.dat"
    act_file_path = os.path.join(MAIN_DIR, "bin")

    data_setter_act = RawDataSetter(file_name=os.path.join(act_file_path, act_file_name),
                                    size_file_m=[256, 256, 750], pixel_size=1, pixel_size_axial=1)
    data_setter_act.read_files()
    return data_setter_act.volume


def fill_dict():
    """Inject volume and activity data from activity map into dictionary"""
    data = MiceData(retrieve_mice_data(), retrieve_activity_data(), retrieve_atlas_data())
    return data.get_activity_organs()


def main():
    root = tk.Tk()
    root.withdraw()
    
    # Copied values to make execution faster. To be removed in final version
    mice_dict = {'External capsule': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Caudateputamen': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Hippocampus': {'SUV_mean': 1.39, 'name_moby': 'hippo_activity', 'id': 43, 'volume': 0.03329708224999999, 'activity': 0.8600082524324324}, 'Anterior commissure': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Globus pallidus': {'SUV_mean': 1.49, 'name_moby': 'globus_pallidus_activity', 'id': 56, 'volume': 0.0029876524999999997, 'activity': 0.9218793497297296}, 'Internal capsule': {'SUV_mean': 1.49, 'name_moby': 'internal_capsule_activity', 'id': 58, 'volume': 0.00394492075, 'activity': 0.9218793497297296}, 'Thalamus': {'SUV_mean': 1.54, 'name_moby': 'thal_activity', 'id': 42, 'volume': 0.015404702124999997, 'activity': 0.9528148983783784}, 'Cerebellum': {'SUV_mean': 1.27, 'name_moby': 'cerebellum_activity', 'id': 38, 'volume': 0.06205476187499999, 'activity': 0.7857629356756756}, 'Superior colliculi': {'SUV_mean': 1.38, 'name_moby': 'superior_colliculus_activity', 'id': 70, 'volume': 0.013459679374999999, 'activity': 0.8538211427027027}, 'Hypothalamus': {'SUV_mean': 1.33, 'name_moby': 'hypothalamus_activity', 'id': 44, 'volume': 0.010417151625, 'activity': 0.822885594054054}, 'Inferior colliculi': {'SUV_mean': 1.29, 'name_moby': 'inferior_colliculus_activity', 'id': 57, 'volume': 0.007310602749999999, 'activity': 0.7981371551351352}, 'Central gray': {'SUV_mean': 1.47, 'name_moby': 'periaqueductal_gray_activity', 'id': 49, 'volume': 0.004545499874999999, 'activity': 0.9095051302702702}, 'Neocortex': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Amygdala': {'SUV_mean': 1.25, 'name_moby': 'amygdala_activity', 'id': 45, 'volume': 0.016858896249999998, 'activity': 0.7733887162162163}, 'Olfactory bulb': {'SUV_mean': 1.44, 'name_moby': 'olfactory_areas_activity', 'id': 65, 'volume': 0.036251199874999994, 'activity': 0.8909438010810811}, 'Brain stem': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Rest of midbrain': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Basal forebrain and septum': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Fimbria': {'SUV_mean': 1.49, 'name_moby': 'fimbria_activity', 'id': 54, 'volume': 0.0028199781249999994, 'activity': 0.9218793497297296}, 'Whole brain': {'SUV_mean': 1.35, 'name_moby': 'brain_activity', 'id': 36, 'volume': 0.007145976999999999, 'activity': 0.8352598135135135}, 'Brain': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Heart': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Lung': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Liver': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Kidney': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}, 'Muscle': {'SUV_mean': 0, 'name_moby': 'None', 'id': 'None', 'volume': 'None', 'activity': 'None'}}
    activity_all_organs = [0.8600082524324324, 0.9218793497297296, 0.9218793497297296, 0.9528148983783784, 0.7857629356756756, 0.8538211427027027, 0.822885594054054, 0.7981371551351352, 0.9095051302702702, 0.7733887162162163, 0.8909438010810811, 0.9218793497297296, 0.8352598135135135, 0]
    volume_all_organs = [0.03329708224999999, 0.0029876524999999997, 0.00394492075, 0.015404702124999997, 0.06205476187499999, 0.013459679374999999, 0.010417151625, 0.007310602749999999, 0.004545499874999999, 0.016858896249999998, 0.036251199874999994, 0.0028199781249999994, 0.007145976999999999, 0]
    normalized_activity_all_organs = [0.07645764576457645, 0.08195819581958194, 0.08195819581958194, 0.08470847084708472, 0.06985698569856985, 0.07590759075907591, 0.07315731573157315, 0.07095709570957096, 0.08085808580858085, 0.06875687568756876, 0.07920792079207921, 0.08195819581958194, 0.07425742574257425, 0.0]
    # activity_all_organs, volume_all_organs, normalized_activity_all_organs, mice_dict = fill_dict()

    # Select organs to get results. To check for all, uncomment the line below
    organs_of_interest = ["Hippocampus"]
    # organs_of_interest = [organ for organ in mice_dict.keys() if mice_dict[organ]["id"] != "None"]

    atlas_volume = retrieve_atlas_data()
    activity_volume = retrieve_activity_data()
    atlas_volume = atlas_volume[50:-50,50:-50,550:]
    activity_volume = activity_volume[50:-50,50:-50,550:]
    segmenter = Segmentation(mice_dict, activity_volume, normalized_activity_all_organs)

    # Segmentation methods. Uncomment the one to use
    segmented_volume = segmenter.k_means()
    # segmented_volume = segmenter.gaussian()
    # segmented_volume = segmenter.bayesian_gaussian()
    
    # Uncomment if necessary
    # visualizer = ImageVisualizer(segmented_volume)
    # visualizer.max_image(ax=1)
    # plt.show()
    
    # Get metrics for all organs and the segmented image
    for organ in organs_of_interest:
    
        truth = GroundTruth(activity_volume, atlas_volume, mice_dict)
        ground_truth_mask, ground_truth = truth.get_ground_truth([organ])

        interest_region = RegionInterest(activity_volume, segmented_volume, ground_truth_mask, ground_truth)
        segmented_image = interest_region.determine_best_fit()
        # segmented_image = segmented_volume
        # segmented_image[segmented_image !=10] =0
        temp = Metrics(ground_truth, segmented_image)
        SNR, MSE, MAE, VOLUME = temp.get_metrics()

        print("Organ:", organ)
        print("MAE:", MAE)
        print("MSE:", MSE)
        print("SNR:", SNR)
        print("volume:", VOLUME)

        visualizer = ImageVisualizer(segmented_image)
        visualizer.max_image(ax=1)

        w = RawDataSetter(os.path.join(MAIN_DIR, "bin", "generated"), volume=activity_volume)
        w.write_files_simple_binary()
        plt.title("Organ: " + organ)
    plt.show()


if __name__ == "__main__":
    main()

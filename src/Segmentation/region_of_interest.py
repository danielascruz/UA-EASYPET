import matplotlib.pyplot as plt
import numpy
import numpy as np


class RegionInterest:
    def __init__(self, act_data, segmentation_data, ground_truth_mask, activity_all_organs):
        self.act_data = act_data
        self.segmentation_data = segmentation_data
        self.ground_truth_mask = ground_truth_mask
        self.activity_all_organs = activity_all_organs
        self.segmented_image = None

    def kmeans_calculate_roi(self):
        result = self.ground_truth_mask * self.segmentation_data
        segmentation_volume = np.copy(self.segmentation_data[:, :, :])
        volume = np.copy(result[:, :, :])

        number_organs = 16
        biggest_cluster = 0
        number_voxels = 0

        plt.figure()
        plt.imshow(np.max(volume[:, :, :], axis=1))
        plt.title("Result: ")
        plt.show()

        for i in range(1, number_organs):
            voxels_cluster = len(volume[volume == i])

            if voxels_cluster > number_voxels:
                biggest_cluster = i
                number_voxels = voxels_cluster

        segmentation_volume[segmentation_volume != biggest_cluster] = 0
        segmentation_volume[segmentation_volume != 0] = 1
        plt.figure()
        plt.imshow(np.max(segmentation_volume[:, :, :], axis=1))
        plt.title("Result: ")
        plt.show()

        self.segmented_image = segmentation_volume * self.act_data

    def bayesian_calculate_roi(self):
        result = self.ground_truth_mask * self.segmentation_data
        segmentation_volume = np.copy(self.segmentation_data[:, :, :])
        volume = np.copy(result[:, :, :])

        segmentation_volume = np.round(segmentation_volume, 6)
        volume = np.round(volume, 6)

        plt.figure()
        plt.imshow(np.max(volume[:, :, :], axis=1))
        plt.title("Result: ")
        plt.show()

        biggest_activity_value = 0
        number_voxels = 0
        for i in np.round(self.activity_all_organs, 6):

            if i != 0:  # Activity of background
                voxels_cluster = len(volume[i - 0.00001 < volume < i + 0.00001])

                if voxels_cluster > number_voxels:
                    biggest_activity_value = i
                    number_voxels = voxels_cluster

        plt.figure()
        plt.imshow(np.max(segmentation_volume[:, :, :], axis=1))
        plt.title("Result: ")
        plt.show()
        segmentation_volume[segmentation_volume != biggest_activity_value] = 0
        segmentation_volume[segmentation_volume != 0] = 1
        plt.figure()
        plt.imshow(np.max(segmentation_volume[:, :, :], axis=1))
        plt.title("Result: ")
        plt.show()

        self.segmented_image = segmentation_volume * self.act_data






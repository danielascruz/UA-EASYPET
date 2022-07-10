import matplotlib.pyplot as plt
import numpy
import numpy as np


class RegionInterest:
    def __init__(self, act_data, segmentation_data, ground_truth_mask, activity_all_organs):
        self.act_data = act_data
        self.segmentation_data = segmentation_data
        self.ground_truth_mask = ground_truth_mask
        self.activity_all_organs = activity_all_organs

    def determine_best_fit(self):
        """
        Determines the cluster with highest probability to correspond to the structure.
        It does this by isolating the target clusters with the ground truth mask, and
        then it chooses the biggest cluster within this volume.

        The biggest cluster (the best fit), is represented by its whole volume, not only
        the volume inside the wanted region.
        """
        result = self.ground_truth_mask * self.segmentation_data
        segmentation_volume = np.copy(self.segmentation_data[:, :, :])
        volume = np.copy(result[:, :, :])

        number_organs = 16
        biggest_cluster = 0
        number_voxels = 0

        for i in range(1, number_organs):
            voxels_cluster = len(volume[volume == i])

            if voxels_cluster > number_voxels:
                biggest_cluster = i
                number_voxels = voxels_cluster

        segmentation_volume[segmentation_volume != biggest_cluster] = 0
        segmentation_volume[segmentation_volume != 0] = 1

        return segmentation_volume * self.act_data
import numpy as np
import matplotlib.pyplot as plt


class GroundTruth:
    def __init__(self, activity_volume, atlas_volume, mice_dict):
        self.activity_volume = activity_volume 
        self.atlas_volume = atlas_volume 
        self.mice_dict = mice_dict

    def get_ground_truth(self, organs):
        atlas_copy = np.copy(self.atlas_volume[:, :, :])
        roi = np.zeros((256, 256, 750))

        for organ in organs:
            atlas_copy[atlas_copy!= self.mice_dict[organ]["id"]] = 0
            roi += atlas_copy
            atlas_copy = np.copy(self.atlas_volume[:, :, :])

        # Mask for ground truth
        roi[roi != 0] = 1
        ground_truth = roi * self.activity_volume

        return roi, ground_truth


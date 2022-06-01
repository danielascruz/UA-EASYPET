import numpy as np


class GroundTruth:
    def __init__(self, act_data, atlas_data, mice_dict):
        self.act_data = act_data
        self.atlas_data = atlas_data
        self.mice_dict = mice_dict
        self.roi = None

    def get_ground_truth(self, organs):
        volume = np.copy(self.atlas_data[:, :, :])

        self.roi = np.zeros((256, 256, 750))
        for i in organs:
            volume[volume != self.mice_dict[i]["id"]] = 0
            self.roi += volume

        self.roi[self.roi != 0] = 1
        self.act_data = self.roi * self.act_data

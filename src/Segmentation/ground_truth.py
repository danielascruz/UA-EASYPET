import numpy as np


class GroundTruth:
    def __init__(self, act_data, atlas_data, mice_dict, voxel_volume, total_activity):
        self.act_data = act_data
        self.atlas_data = atlas_data
        self.mice_dict = mice_dict
        self.roi = None
        self.voxel_volume = voxel_volume
        self.total_weight = self.calculate_mice_weight()
        self.total_activity = total_activity

    def calculate_mice_weight(self):
        volume = np.copy(self.atlas_data[:, :, :])
        number_voxels = len(volume[volume != 0])
        mice_volume = number_voxels * self.voxel_volume
        DENSITY = 1
        return mice_volume * DENSITY

    def get_ground_truth(self, organs):
        volume = np.copy(self.atlas_data[:, :, :])

        self.roi = np.zeros((256, 256, 750))
        for i in organs:
            volume[volume != self.mice_dict[i]["id"]] = 0
            self.roi += volume

            # Volume of each organ
            number_voxels = len(volume[volume != 0])
            self.mice_dict[i]["volume"] = number_voxels * self.voxel_volume

            # Activity of each organ
            self.mice_dict[i]["activity"] = \
                self.mice_dict[i]["SUV_mean"] * self.total_weight / self.total_activity / self.voxel_volume
            volume = np.copy(self.atlas_data[:, :, :])

        self.roi[self.roi != 0] = 1
        self.act_data = self.roi * self.act_data

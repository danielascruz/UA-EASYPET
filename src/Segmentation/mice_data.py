import numpy as np


class MiceData:
    def __init__(self, mice_dict, act_data, atlas_data, voxel_volume, total_activity):
        self.act_data = act_data
        self.atlas_data = atlas_data
        self.mice_dict = mice_dict
        self.voxel_volume = voxel_volume
        self.total_weight = self.calculate_mice_weight()
        self.total_activity = total_activity
        self.activity_all_organs = []
        self.volume_all_organs = []

    def calculate_mice_weight(self):
        volume = np.copy(self.atlas_data[:, :, :])
        number_voxels = len(volume[volume != 0])
        mice_volume = number_voxels * self.voxel_volume
        DENSITY = 1
        return mice_volume * DENSITY

    def get_activity_organs(self):
        volume = np.copy(self.atlas_data[:, :, :])

        for i in self.mice_dict.keys():
            if self.mice_dict[i]["name_moby"] != "None":
                # Volume of each organ
                volume[volume != self.mice_dict[i]["id"]] = 0
                number_voxels = len(volume[volume != 0])
                self.mice_dict[i]["volume"] = number_voxels * self.voxel_volume

                # Activity of each organ
                self.mice_dict[i]["activity"] = \
                self.mice_dict[i]["SUV_mean"] * self.total_weight / self.total_activity / self.voxel_volume

                self.activity_all_organs.append(self.mice_dict[i]["activity"])
                self.volume_all_organs.append(self.mice_dict[i]["volume"])

                # Restore the initial volume to calculate other volumes and activities
                volume = np.copy(self.atlas_data[:, :, :])

        # Activity and volume of background
        self.activity_all_organs.append(0)
        self.volume_all_organs.append(0)

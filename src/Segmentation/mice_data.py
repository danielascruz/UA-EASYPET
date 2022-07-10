import numpy as np

VOXEL_VOLUME = (0.145 * 0.145 * 0.145) * 0.001  # cm^3 -> mL
ACTIVITY_INJECTED = 18500000

class MiceData:
    def __init__(self, mice_dict, act_data, atlas_data):
        self.act_data = act_data
        self.atlas_data = atlas_data
        self.mice_dict = mice_dict
        self.total_weight = self.calculate_mice_weight()

    def calculate_mice_weight(self):
        volume = np.copy(self.atlas_data[:, :, :])
        number_voxels = len(volume[volume != 0])
        mice_volume = number_voxels * VOXEL_VOLUME
        DENSITY = 1
        return mice_volume * DENSITY

    def get_activity_organs(self):
        volume = np.copy(self.atlas_data[:, :, :])

        activity_all_organs = []
        normalized_activity_all_organs = []
        volume_all_organs = []
        for i in self.mice_dict.keys():
            if self.mice_dict[i]["name_moby"] != "None":
                # Volume of each organ
                volume[volume != self.mice_dict[i]["id"]] = 0
                number_voxels = len(volume[volume != 0])
                self.mice_dict[i]["volume"] = number_voxels * VOXEL_VOLUME

                # Activity of each organ
                self.mice_dict[i]["activity"] = \
                self.mice_dict[i]["SUV_mean"] * self.total_weight / ACTIVITY_INJECTED / VOXEL_VOLUME

                activity_all_organs.append(self.mice_dict[i]["activity"])
                volume_all_organs.append(self.mice_dict[i]["volume"])

                # Restore the initial volume to calculate other volumes and activities
                volume = np.copy(self.atlas_data[:, :, :])

        # Activity and volume of background
        activity_all_organs.append(0)
        volume_all_organs.append(0)

        # Normalize activity
        normalizer = sum(activity_all_organs)
        for activity in activity_all_organs:
            normalized_activity_all_organs.append(activity/normalizer)

        return activity_all_organs, volume_all_organs, normalized_activity_all_organs, self.mice_dict

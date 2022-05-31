import matplotlib.pyplot as plt
import numpy as np


class RegionInterest:
    def __init__(self, act_data, segmentation_data, ground_truth_mask):
        self.act_data = act_data
        self.segmentation_data = segmentation_data
        self.ground_truth_mask = ground_truth_mask
        self.segmented_image = None

    def region_to_segment(self):
        result = self.ground_truth_mask * self.segmentation_data
        # result[result != 0] = 1
        # result = result * self.act_data

        # Errado porque dentro do result existem vários grupos, tenho de contar o maior número de contagens do grupo x
        # e depois disso, isolar o grupo x na imagem segmentada, tornar isso numa máscara binária e multiplicar pela
        # atividade original

        # number_clusters = len(np.unique(result))
        # print("Número de clusters resultante da multiplicação:", number_clusters)

        segmentation_volume = np.copy(self.segmentation_data[:, :, :])
        volume = np.copy(result[:, :, :])

        plt.figure()
        plt.imshow(np.max(result[:, :, :], axis=1))
        plt.show()

        number_organs = 15
        biggest_cluster = 0
        number_voxels = 0
        for i in range(1, number_organs):
            voxels_cluster = len(volume[volume == i])

            if voxels_cluster > number_voxels:
                biggest_cluster = i
                number_voxels = voxels_cluster

        segmentation_volume[segmentation_volume != biggest_cluster] = 0
        segmentation_volume[segmentation_volume != 0] = 1

        self.segmented_image = segmentation_volume * self.act_data

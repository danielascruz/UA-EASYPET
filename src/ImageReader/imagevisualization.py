import matplotlib.pyplot as plt
import numpy as np


class ImageVisualizer:
    def __init__(self, data=None):
        self.data = data

    def sum_image(self, ax=0):
        plt.imshow(np.sum(self.data.volume[:, :, :], axis=ax))
        plt.show()

    def max_image(self, ax=0):
        plt.imshow(np.max(self.data.volume[:, :, :], axis=ax))
        plt.show()

    def organ(self, i=0, ax=0):
        volume = np.copy(self.data.volume[:, :, :])
        volume[volume != i] = 0
        plt.imshow(np.max(volume, axis=ax))
        plt.show()

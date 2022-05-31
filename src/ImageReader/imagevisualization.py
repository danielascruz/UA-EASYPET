import matplotlib.pyplot as plt
import numpy as np


class ImageVisualizer:
    def __init__(self, data=None):
        self.data = data

    def sum_image(self, ax=0):
        plt.imshow(np.sum(self.data[:, :, :], axis=ax))

    def max_image(self, ax=0):
        plt.imshow(np.max(self.data[:, :, :], axis=ax))

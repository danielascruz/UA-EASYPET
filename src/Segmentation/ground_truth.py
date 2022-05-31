import matplotlib.pyplot as plt
import numpy as np


class GroundTruth:
    def __init__(self, data, atlas):
        self.data = data
        self.atlas = atlas

    def ground_truth(self, organs=None):
        volume = np.copy(self.data.volume[:, :, :])
        roi = np.zeros((256, 256, 750))
        for i in organs:
            volume[volume != i] = 0
            roi = roi + volume
            volume = np.copy(self.data.volume[:, :, :])

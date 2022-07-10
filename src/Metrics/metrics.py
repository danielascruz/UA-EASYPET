from skimage import metrics
import numpy as np


class Metrics:
    def __init__(self, ground_truth, segmented_image):
        self.ground_truth = ground_truth
        self.segmented_image = segmented_image

    def get_metrics(self):
        normalized_truth = self.ground_truth / (np.max(self.ground_truth[:, :, :]))
        normalized_image = self.segmented_image / (np.max(self.ground_truth[:, :, :]))
        number_voxels = len(self.segmented_image[self.segmented_image != 0])

        SNR = metrics.peak_signal_noise_ratio(normalized_truth, normalized_image)
        MSE = metrics.mean_squared_error(normalized_truth, normalized_image)
        MAE = self.get_mae()
        VOLUME = np.round(number_voxels * (0.145 * 0.145 * 0.145) * 0.001, 6)

        return SNR, MSE, MAE, VOLUME

    def get_mae(self):
        flat_ground_truth = np.asarray(flatten_matrix(self.ground_truth))
        flat_segmented = np.asarray(flatten_matrix(self.segmented_image))
        return np.mean(np.abs(flat_segmented - flat_ground_truth))

def flatten_matrix(matrix):
    res = []
    for i in matrix:
        for j in i:
            for k in j:
                res.append(k)
    return res

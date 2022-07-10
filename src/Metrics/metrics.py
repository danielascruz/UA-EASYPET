from skimage import metrics
import numpy as np
from sklearn import metrics as skmetrics


class Metrics:
    def __init__(self, ground_truth, segmented_image):
        self.ground_truth = ground_truth
        self.segmented_image = segmented_image
        self.SNR = None
        self.MSE = None
        self.MAE = None
        self.volume = None
        self.test = None
        self.test2 = None
        self.mse = None

    def get_metrics(self):
        max = np.max(self.ground_truth)
        max2 = np.max(self.ground_truth[:, :, :])
        normalized_truth = self.ground_truth / (np.max(self.ground_truth[:, :, :]))
        normalized_image = self.segmented_image / (np.max(self.ground_truth[:, :, :]))

        self.SNR = metrics.peak_signal_noise_ratio(normalized_truth, normalized_image)
        self.MSE = metrics.mean_squared_error(normalized_truth, normalized_image)

        number_voxels = len(self.segmented_image[self.segmented_image != 0])
        self.volume = number_voxels * (0.145 * 0.145 * 0.145) * 0.001
        self.volume = np.round(self.volume, 6)

    def get_mae(self):
        flat_ground_truth = np.asarray(flatten_matrix(self.ground_truth))
        flat_segmented = np.asarray(flatten_matrix(self.segmented_image))
        self.MAE = np.mean(np.abs(flat_segmented - flat_ground_truth))

    def calculate_psnr(self):
        """"Calculating peak signal-to-noise ratio (PSNR) between two images."""
        normalized_truth = self.ground_truth/(np.max(self.ground_truth[:, :, :]))
        normalized_image = self.segmented_image / (np.max(self.ground_truth[:, :, :]))

        self.mse = np.mean((np.array(normalized_truth, dtype=np.float32) - np.array(normalized_image, dtype=np.float32)) ** 2)
        if self.mse == 0:
            self.test = 100
        self.test = 20 * np.log10(1/(np.sqrt(self.mse)))
        self.test2 = 10 * np.log10(np.max(normalized_truth)**2 / self.mse)


def flatten_matrix(matrix):
    res = []
    for i in matrix:
        for j in i:
            for k in j:
                res.append(k)
    return res

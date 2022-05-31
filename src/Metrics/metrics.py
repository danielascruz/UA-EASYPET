import skimage
from skimage import metrics


class Metrics:
    def __init__(self, ground_truth, segmented_image):
        self.ground_truth = ground_truth
        self.segmented_image = segmented_image
        self.SNR = None
        self.NRMSE = None
    # Covariance; Signal Noise Ratio; Normalized Mean Squared Error or Mean Squared Error; Normalized Standard Deviation
    # or Standard Deviation;
    # PET: Recovery Coefficient (CRC ou RC)

    def get_metrics(self):
        self.SNR = skimage.metrics.peak_signal_noise_ratio(self.ground_truth, self.segmented_image)
        self.NRMSE = skimage.metrics.normalized_root_mse(self.ground_truth, self.segmented_image)

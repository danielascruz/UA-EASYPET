import matplotlib.pyplot as plt
from skimage import measure
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture, BayesianGaussianMixture


class Segmentation:
    def __init__(self, mice_dict, act_data, organs_activity):
        self.mice_dict = mice_dict
        self.act_data = act_data
        self.organs_activity = organs_activity
        self.volume = None
        self.result = None
        self.segmentation = None

    def k_means(self):
        self.volume = np.copy(self.act_data[:, :, :])
        layer = self.volume[:, :, :]
        sum_all = np.sum(layer)
        layer = layer/sum_all

        self.segmentation = np.zeros(self.volume.shape)

        x = np.arange(self.volume.shape[0])
        y = np.arange(self.volume.shape[1])
        z = np.arange(self.volume.shape[2])

        # Create 3 EMPTY arrays with images size.
        im_index_x = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))
        im_index_y = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))
        im_index_z = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))

        # Repeat values in one direction. Like x_axis only grows in x_axis (0, 1, 2 ... number of pixels)
        # but repeat these values on y an z axis
        im_index_x[:] = x[..., None, None]
        im_index_y[:] = y[None, ..., None]
        im_index_z[:] = z[None, None, ...]

        matriz = np.zeros((len(layer[layer != 0]), 3))
        weights = layer[layer != 0]

        matriz[:, 0] = im_index_x[layer != 0]
        matriz[:, 1] = im_index_y[layer != 0]
        matriz[:, 2] = im_index_z[layer != 0]

        kmeans = KMeans(n_clusters=16, init='k-means++', max_iter=300, n_init=10, random_state=0)
        test = kmeans.fit_predict(matriz, weights)
        matriz = matriz.astype(int)
        for element in range(len(test)):
            self.segmentation[matriz[element, 0], matriz[element, 1], matriz[element, 2]] = test[element]

    def gaussian(self):
        self.volume = np.copy(self.act_data[:, :, :])
        layer = self.volume[:, :, :]
        sum_all = np.sum(layer)
        layer = layer/sum_all

        self.segmentation = np.zeros(self.volume.shape)

        x = np.arange(self.volume.shape[0])
        y = np.arange(self.volume.shape[1])
        z = np.arange(self.volume.shape[2])

        # Create 3 EMPTY arrays with images size.
        im_index_x = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))
        im_index_y = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))
        im_index_z = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))

        # Repeat values in one direction. Like x_axis only grows in x_axis (0, 1, 2 ... number of pixels)
        # but repeat these values on y an z axis
        im_index_x[:] = x[..., None, None]
        im_index_y[:] = y[None, ..., None]
        im_index_z[:] = z[None, None, ...]

        matriz = np.zeros((len(layer[layer != 0]), 3))
        weights = layer[layer != 0]

        matriz[:, 0] = im_index_x[layer != 0]
        matriz[:, 1] = im_index_y[layer != 0]
        matriz[:, 2] = im_index_z[layer != 0]

        gaussian = GaussianMixture(n_components=16, covariance_type="diag", weights_init=self.organs_activity)
        fit_test = gaussian.fit(matriz, weights)
        test = gaussian.predict(matriz)
        matriz = matriz.astype(int)
        for element in range(len(test)):
            self.segmentation[matriz[element, 0], matriz[element, 1], matriz[element, 2]] = test[element]

    def bayesian_gaussian(self):
        self.volume = np.copy(self.act_data[:, :, :])
        layer = self.volume[:, :, :]
        sum_all = np.sum(layer)
        layer = layer/sum_all

        self.segmentation = np.zeros(self.volume.shape)

        x = np.arange(self.volume.shape[0])
        y = np.arange(self.volume.shape[1])
        z = np.arange(self.volume.shape[2])

        # Create 3 EMPTY arrays with images size.
        im_index_x = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))
        im_index_y = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))
        im_index_z = np.ascontiguousarray(np.empty(self.volume.shape, dtype=np.int32))

        # Repeat values in one direction. Like x_axis only grows in x_axis (0, 1, 2 ... number of pixels)
        # but repeat these values on y an z axis
        im_index_x[:] = x[..., None, None]
        im_index_y[:] = y[None, ..., None]
        im_index_z[:] = z[None, None, ...]

        matriz = np.zeros((len(layer[layer != 0]), 4))
        weights = layer[layer != 0]

        matriz[:, 0] = im_index_x[layer != 0]
        matriz[:, 1] = im_index_y[layer != 0]
        matriz[:, 2] = im_index_z[layer != 0]
        matriz[:, 3] = weights

        gaussian = BayesianGaussianMixture(n_components=16, random_state=1, covariance_type='full')
        fit_test = gaussian.fit(matriz)
        test = gaussian.predict(matriz)
        matriz = matriz.astype(int)
        for element in range(len(test)):
            self.segmentation[matriz[element, 0], matriz[element, 1], matriz[element, 2]] = test[element]


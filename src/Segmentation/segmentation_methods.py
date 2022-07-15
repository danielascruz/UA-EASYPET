import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture, BayesianGaussianMixture


class Segmentation:
    def __init__(self, mice_dict, activity_volume, organs_activity):
        self.mice_dict = mice_dict
        self.activity_volume = activity_volume
        self.organs_activity = organs_activity

    def setup_kmeans_gaussian(self):
        """
        Create matrices and weights to be used in both the k-means
        and gaussian mixture methods. Since the setup for bayesian
        gaussian is slightly different, it could not be refactored
        into this function.
        """
        volume = np.copy(self.activity_volume[:, :, :])
        layer = volume[:, :, :]
        sum_all = np.sum(layer)
        layer = layer / sum_all

        self.segmentation = np.zeros(volume.shape)

        x = np.arange(volume.shape[0])
        y = np.arange(volume.shape[1])
        z = np.arange(volume.shape[2])

        # Create 3 EMPTY arrays with images size.
        im_index_x = np.ascontiguousarray(np.empty(volume.shape, dtype=np.int32))
        im_index_y = np.ascontiguousarray(np.empty(volume.shape, dtype=np.int32))
        im_index_z = np.ascontiguousarray(np.empty(volume.shape, dtype=np.int32))

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

        return matriz, weights

    def k_means(self):
        matriz, weights = self.setup_kmeans_gaussian()
        kmeans = KMeans(n_clusters=14, init='k-means++', max_iter=500, n_init=10, random_state=0)
        test = kmeans.fit_predict(matriz, sample_weight=weights)
        matriz = matriz.astype(int)
        for element in range(len(test)):
            self.segmentation[matriz[element, 0], matriz[element, 1], matriz[element, 2]] = test[element]

        return self.segmentation

    def gaussian(self):
        matriz, weights = self.setup_kmeans_gaussian()
        gaussian = GaussianMixture(n_components=14, weights_init=self.organs_activity)
        test = gaussian.fit_predict(matriz, weights)
        # test = gaussian.predict(matriz)
        matriz = matriz.astype(int)
        for element in range(len(test)):
            self.segmentation[matriz[element, 0], matriz[element, 1], matriz[element, 2]] = test[element]

        return self.segmentation

    def bayesian_gaussian(self):
        volume = np.copy(self.activity_volume[:, :, :])
        layer = volume[:, :, :]
        sum_all = np.sum(layer)
        layer = layer / sum_all


        self.segmentation = np.zeros(volume.shape)
        # layer[layer>0.9*layer.max()] = 0
        x = np.arange(volume.shape[0])
        y = np.arange(volume.shape[1])
        z = np.arange(volume.shape[2])

        # Create 3 EMPTY arrays with images size.
        im_index_x = np.ascontiguousarray(np.empty(volume.shape, dtype=np.int32))
        im_index_y = np.ascontiguousarray(np.empty(volume.shape, dtype=np.int32))
        im_index_z = np.ascontiguousarray(np.empty(volume.shape, dtype=np.int32))

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
        matriz_teste = np.zeros((len(layer[layer != 0]), 4))
        matriz_teste[:, 0] = weights*1000000
        # matriz_teste[:, 1] = im_index_z[layer != 0]
        # matriz_teste[:, 2] = im_index_y[layer != 0]
        # matriz_teste[:, 2] = im_index_y[layer != 0]
        # # matriz_teste[:, 3] = 1
        v = np.unique(weights)
        for i in v:
            matriz_teste[weights == i, 1] = i
            matriz_teste[weights == i, 2] = i
            matriz_teste[weights == i, 3] = i
        # matriz_tadd = matriz_teste

        # c = 1
        # for i in v:
        #     b = np.tile(matriz_teste[weights==i] + np.random.rand(int(matriz_teste[weights == i].shape[0]),int(matriz_teste[weights == i].shape[1]))/c, (5, 1))
        #
        #     matriz_tadd = np.vstack((matriz_tadd,b))
        #
        #     c +=1
        # matriz_teste = matriz_tadd
        # matriz_teste[:, 2] = weights
        # matriz_teste[:, 3] = weights
        gaussian = BayesianGaussianMixture(n_components=11, random_state=1, n_init=1, max_iter=500,
                                           verbose=1, covariance_type="spherical")
        # fit_test = gaussian.fit(matriz)
        test = gaussian.fit_predict(matriz_teste)

        # test = gaussian.predict(matriz)
        # matriz = matriz_teste
        matriz = matriz.astype(int)
        for element in range(len(test)):
            self.segmentation[matriz[element, 0], matriz[element, 1], matriz[element, 2]] = test[element]

        return self.segmentation


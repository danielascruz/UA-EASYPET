import os
import matplotlib.pyplot as plt
import skimage
import numpy as np
from skimage.metrics import peak_signal_noise_ratio
from skimage import feature
from skimage.color import rgb2gray, rgb2hsv
from skimage.filters import threshold_otsu
from skimage.io import imshow

directory = os.path.dirname(os.path.abspath(__file__))
image = plt.imread(os.path.join(directory, "image", "fruta-1024x676.jpg"))

grayscale = rgb2gray(image)
edges1 = feature.canny(grayscale)
edges2 = feature.canny(grayscale, 2)

fig, axes = plt.subplots(1, 3, figsize=(8, 3))

axes[0].imshow(grayscale, cmap='gray')
axes[0].axis('off')
axes[0].set_title('Original (GrayScale)')

axes[1].imshow(edges1, cmap='gray')
axes[1].axis('off')
axes[1].set_title("Edges with Canny, sigma=1")

axes[2].imshow(edges2, cmap='gray')
axes[2].axis('off')
axes[2].set_title("Edges with Canny, sigma=2")

fig.tight_layout()
plt.show()

# --- COLOR IMAGE SEGMENTATION WITH HSV ---
image_hsv = rgb2hsv(image)

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].imshow(image_hsv[:, :, 0], cmap='gray')
ax[0].set_title('Hue')
ax[1].imshow(image_hsv[:, :, 1], cmap='gray')
ax[1].set_title('Saturation')
ax[2].imshow(image_hsv[:, :, 2], cmap='gray')
ax[2].set_title('Value')

plt.show()

# Need to obtain the intensity values of each HSV channel, with a colorbar.
fig_color, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(image_hsv[:, :, 0], cmap='hsv')
ax[0].set_title('hue')
ax[1].imshow(image_hsv[:, :, 1], cmap='hsv')
ax[1].set_title('transparency')
ax[2].imshow(image_hsv[:, :, 2], cmap='hsv')
ax[2].set_title('value')

fig_color.colorbar(imshow(image_hsv[:, :, 0], cmap='hsv'))
fig_color.tight_layout()
plt.show()

# refer to hue channel (in the colorbar)
lower_mask = image_hsv[:, :, 0] > 0.9
upper_mask = image_hsv[:, :, 0] < 1
# refer to transparency channel (in the colorbar)
saturation_mask = image_hsv[:, :, 1] > 0.95
mask = upper_mask * lower_mask * saturation_mask

red = image[:, :, 0] * mask
green = image[:, :, 1] * mask
blue = image[:, :, 2] * mask
image_masked = np.dstack((red, green, blue))
plt.imshow(image_masked)
plt.show()

# --- TODO COLOR IMAGE SEGMENTATION WITH CV ---

# --- THRESHOLDING METHODS ---
# Otsu's
otsu = threshold_otsu(grayscale)
binary_otsu = grayscale > otsu
# TODO Represent the original image and the result of Otsu's Method
# --- Metrics ---
# Covariance; Signal Noise Ratio; Normalized Mean Squared Error or Mean Squared Error; Normalized Standard Deviation
# or Standard Deviation;
# PET: Recovery Coefficient (CRC ou RC)
# SNR
SNR_otsu = skimage.metrics.peak_signal_noise_ratio(grayscale, binary_otsu)
print("The peak signal to noise ratio, for Otsu's method, is:", SNR_otsu)
MSE_otsu = skimage.metrics.mean_squared_error(grayscale, binary_otsu)
print("The mean-squared error between the images, for Otsu's method is:", MSE_otsu)
NRMSE_otsu = skimage.metrics.normalized_root_mse(grayscale, binary_otsu)
print("The normalized root mean-squared error between the images, for Otsu's method is:", NRMSE_otsu)
STD_image = np.std(image)
STD_otsu = np.std(binary_otsu)
print("The standard deviation for the original image is:", STD_image, "and for the thresholded image (Otsu's method) "
                                                                      "is:", STD_otsu)


def covariance_otsu(x, y):
    x_bar, y_bar = x.mean(), y.mean()
    return np.sum((grayscale - x_bar)*(y - y_bar))/(len(x) - 1)


print("The covariance between the images, for Otsu's method is:", covariance_otsu(grayscale, binary_otsu))

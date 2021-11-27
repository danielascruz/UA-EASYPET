# Thresholding is used to create a binary image from a grayscale image
# Otsu’s method calculates an “optimal” threshold (marked by a red line in the histogram below)
# by maximizing the variance between two classes of pixels, which are separated by the threshold.
# Equivalently, this threshold minimizes the intra-class variance.

import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu

image = data.camera()
thresh = threshold_otsu(image)
binary = image > thresh  # parecido a uma máscara, todos os valores de images maiores que thresh ficam True.

fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
ax = axes.ravel()

ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 2)
ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])   # partilham eixos, para ficar na mesma escala etc

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

ax[2].imshow(binary, cmap=plt.cm.gray)
ax[2].set_title('Thresholded')
ax[2].axis('off')

plt.show()

# Se não souber qual o método de Thresholding adequado:
from skimage.filters import try_all_threshold

img = data.page()

# Here, we specify a radius for local thresholding algorithms.
# If it is not specified, only global algorithms are called.
fig, ax = try_all_threshold(img, figsize=(10, 8), verbose=False)
plt.show()

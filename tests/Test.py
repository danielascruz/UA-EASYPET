from skimage import data, filters
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.filters import threshold_otsu, try_all_threshold, threshold_multiotsu
import numpy as np
from skimage.filters.thresholding import _cross_entropy
import os

# --- EDGES ---
image = data.cat()
edges = filters.sobel(image)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
# ax = axes.ravel()

axes[0].imshow(image)
axes[0].set_title("Original")
axes[0].set_axis_off()

axes[1].imshow(edges)
axes[1].set_title("Edges")
axes[1].set_axis_off()

fig.tight_layout()
plt.show()

# --- RGB TO GRAY ---
grayscale = rgb2gray(image)  # transform into grayscale
fig, axes = plt.subplots(1, 2, figsize=(8, 4))

axes[0].imshow(image)
axes[0].set_title("Original")
axes[0].set_axis_off()

axes[1].imshow(grayscale, cmap='gray')  # equal to cmap=plt.cm.gray
axes[1].set_title("Grayscale")
axes[1].axis('off')

fig.tight_layout()
plt.show()

# --- RESCALE ---
# Rescale resizes an image by a given scaling factor. Resize serves the same purpose, but allows to specify an output
# image shape instead of a scaling factor. Downscale serves the purpose of down-sampling an n-dimensional image by
# integer factors using the local mean on the elements of each block of the size factors given as a parameter to the
# function.
# Anti_aliasing: apply a Gaussian filter to smooth the image.

grayscale_rescaled = rescale(grayscale, 0.25, anti_aliasing=False)
grayscale_resized = resize(grayscale, (grayscale.shape[0] // 4, grayscale.shape[1] // 4), anti_aliasing=False)
grayscale_downscaled = downscale_local_mean(grayscale, (4, 3))

fig, axes = plt.subplots(nrows=2, ncols=2)
ax = axes.ravel()

ax[0].imshow(grayscale, cmap='gray')
ax[0].set_title("Original")

ax[1].imshow(grayscale_rescaled, cmap='gray')
ax[1].set_title("Rescaled image (with aliasing)")

ax[2].imshow(grayscale_resized, cmap='gray')
ax[2].set_title("Resized image (with aliasing)")

ax[3].imshow(grayscale_downscaled, cmap='gray')
ax[3].set_title("Downscaled image (no aliasing)")

ax[0].set_xlim(0, 512)
ax[0].set_ylim(512, 0)

for a in ax:
    a.set_axis_off()
plt.tight_layout()
plt.show()

# --- THRESHOLDING ---
# Thresholding is used to create a binary image from a grayscale image.
# If I don't know which thresholding method to choose.
# We specify a radius for local thresholding algorithms. If it is not specified, only global algorithms are called.
image = data.camera()
fig, ax = try_all_threshold(image, figsize=(10, 8), verbose=False)

plt.figure()
fig.tight_layout()
plt.show()

# Otsu's Method
thresh = threshold_otsu(image)
binary = image > thresh  # every value bigger than 'thresh' turns True

fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
axt = axes.ravel()

axt[0] = plt.subplot(1, 3, 1)
axt[0].imshow(image, cmap=plt.cm.gray)
axt[0].set_title('Original')
axt[0].axis('off')

axt[1] = plt.subplot(1, 3, 2)
axt[1].hist(image.ravel(), bins=256)
axt[1].set_title('Histogram')
axt[1].axvline(thresh, color='r')

axt[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])   # share their axes
axt[2].imshow(binary, cmap=plt.cm.gray)
axt[2].set_title("Thresholded with Otsu's Method")
axt[2].axis('off')

plt.show()

# --- Li Thresholding Method ---
# They proposed that minimizing the cross-entropy between the foreground and the foreground mean, and the background
# and the background mean, would give the best threshold in most situations.

thresh_li = np.arange(np.min(image) + 1.5, np.max(image) - 1.5)
entropies = [_cross_entropy(image, t) for t in thresh_li]
optimal_camera_threshold = thresh_li[np.argmin(entropies)]  # Returns the indices of the minimum values along an axis.

fig_li, ax_li = plt.subplots(1, 3, figsize=(8, 3))
ax_li[0].imshow(image, cmap='gray')
ax_li[0].set_title('image')
ax_li[0].set_axis_off()

ax_li[1].imshow(image > optimal_camera_threshold, cmap='gray')
ax_li[1].set_title('Thresholded with Li´s Method')
ax_li[1].set_axis_off()

ax_li[2].plot(thresh_li, entropies)
ax_li[2].set_xlabel('thresholds')
ax_li[2].set_ylabel('cross-entropy')
ax_li[2].vlines(optimal_camera_threshold, ymin=np.min(entropies) - 0.05 * np.ptp(entropies),
                ymax=np.max(entropies) - 0.05 * np.ptp(entropies))
ax_li[2].set_title('optimal threshold')

fig_li.tight_layout()

print('The brute force optimal threshold is:', optimal_camera_threshold)
print('The computed optimal threshold is:', filters.threshold_li(image))

plt.show()

# --- Multi-Otsu Method ---
# Thresholding algorithm that is used to separate the pixels of an input image into several different classes,
# each one obtained according to the intensity of the gray levels within the image.
cat = rgb2gray(data.cat())
thresh_multi = threshold_multiotsu(cat)  # Creates 3 classes
regions = np.digitize(cat, bins=thresh_multi)

fig_multi, ax_multi = plt.subplots(1, 3, figsize=(10, 3.5))

ax_multi[0].imshow(cat, cmap='jet')
ax_multi[0].set_title('Original')
ax_multi[0].axis('off')

ax_multi[1].hist(cat.ravel(), bins=255)
ax_multi[1].set_title('Histogram')

ax_multi[2].imshow(regions, cmap='jet')
ax_multi[2].set_title('Multi-Otsu Result')
ax_multi[2].axis('off')

plt.subplots_adjust()
plt.show()


# Covariancia
# std
# SNR
# Normalized mean squared error ou mean squared error
# Normalized standard deviation

# PET: Recovery Coefficient (CRC ou RC)
diretorio = os.path.dirname(os.path.abspath(__file__))
image = plt.imread(os.path.join(diretorio, image, "fruta-1024x676.jpg"))

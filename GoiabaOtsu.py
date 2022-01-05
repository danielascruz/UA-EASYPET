import matplotlib.pyplot as plt
import cv2
import skimage
import numpy as np
from skimage.metrics import peak_signal_noise_ratio

fruit_BGR = cv2.imread('./image/goiaba-43.jpg')
fruit_RGB = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2RGB)
fruit_gray = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(fruit_RGB)
plt.axis('off')
plt.title('Original Image')

# In order to add a black background to the ground truth, need to import the alpha channel (represents the degree of
# transparency) -> BGRA
ground_truth_BGRA = cv2.imread('./image/groundtruth.png', cv2.IMREAD_UNCHANGED)

# Make mask of where the transparent bits are and replace with black bits
trans_mask = ground_truth_BGRA[:, :, 3] == 0
ground_truth_BGRA[trans_mask] = [0, 0, 0, 0]
ground_truth_RGB = cv2.cvtColor(ground_truth_BGRA, cv2.COLOR_BGRA2RGB)  # New image without alpha channel


# Otsu's Method
# Calculate the Otsu's Threshold
threshold_otsu, result_otsu = cv2.threshold(fruit_gray, 0, 255, cv2.THRESH_OTSU)
print("Obtained Threshold: ", threshold_otsu)
result_otsu_RGB = cv2.cvtColor(result_otsu, cv2.COLOR_GRAY2RGB)

mask = np.zeros(fruit_RGB.shape[:2], dtype="uint8")  # All zeros -> zero is black
cv2.circle(mask, (210, 196), 73, 255, -1)
cv2.circle(mask, (350, 205), 75, 255, -1)
result = cv2.bitwise_and(result_otsu_RGB, result_otsu_RGB, mask=mask)

# Final Image
plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(result_otsu_RGB)
plt.axis('off')
plt.title("Thresholded with Otsu's Method")

plt.subplot(2, 1, 2)
plt.imshow(result)
plt.axis('off')
plt.title("Thresholded with Otsu's Method and then applied a mask")
plt.show()

# Metric
SNR_otsu = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result_otsu_RGB)
print("The peak signal to noise ratio, for Otsu's method, is:", SNR_otsu)

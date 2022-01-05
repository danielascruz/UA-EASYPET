import matplotlib.pyplot as plt
import numpy as np
import cv2
import skimage
from skimage.metrics import peak_signal_noise_ratio

fruit_BGR = cv2.imread('./image/goiaba-43.jpg')
fruit_RGB = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2RGB)

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


# Circular mask to apply in original image and isolate the object
mask = np.zeros(fruit_RGB.shape[:2], dtype="uint8")  # All zeros -> zero is black
cv2.circle(mask, (206, 197), 74, 255, -1)
cv2.circle(mask, (352, 206), 76, 255, -1)
result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

SNR = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result)
print("The peak signal to noise ratio is: ", SNR)

plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(ground_truth_RGB)
plt.title('Ground Truth')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(result)
plt.title('Segmentation using masks')
plt.axis('off')

plt.figure()
plt.imshow(mask, cmap='gray')
plt.title('Mask used')
plt.axis('off')
plt.show()

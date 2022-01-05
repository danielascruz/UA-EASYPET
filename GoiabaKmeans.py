import matplotlib.pyplot as plt
import numpy as np
import cv2
import skimage
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


# K-Means
twoDimage = fruit_RGB.reshape((-1, 3))
twoDimage = np.float32(twoDimage)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
attempts = 10
K = 10

ret, label, center = cv2.kmeans(twoDimage, K, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_K = res.reshape(fruit_RGB.shape)

# Apply a mask to crop the objet of interest
mask = np.zeros(fruit_RGB.shape[:2], dtype="uint8")  # All zeros -> zero is black
cv2.circle(mask, (210, 196), 73, 255, -1)
cv2.circle(mask, (350, 205), 75, 255, -1)
result = cv2.bitwise_and(result_K, result_K, mask=mask)

SNR = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result)
print("The peak signal to noise ratio is: ", SNR)

plt.figure()
plt.imshow(result_K)
plt.axis('off')
plt.title('Segmented Image with K-Means without a mask')
plt.show()

plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(ground_truth_RGB)
plt.title('Ground Truth')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(result)
plt.axis('off')
plt.title('Segmented Image with K-Means and then applied a mask')
plt.show()

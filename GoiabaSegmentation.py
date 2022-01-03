import matplotlib.pyplot as plt
import numpy as np
import cv2
import skimage
from skimage.metrics import peak_signal_noise_ratio

fruit_BGR = cv2.imread('./image/goiaba-43.jpg')
fruit_RGB = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2RGB)
fruit_gray = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2GRAY)

ground_truth_BGRA = cv2.imread('./image/groundtruth.png', cv2.IMREAD_UNCHANGED)  # In order to add a black background to
# the ground truth, I need to import the alpha channel (represents the degree of transparency) -> BGRA

# Make mask of where the transparent bits are and replace with black bits
trans_mask = ground_truth_BGRA[:, :, 3] == 0
ground_truth_BGRA[trans_mask] = [0, 0, 0, 0]
# New image without alpha channel
ground_truth_RGB = cv2.cvtColor(ground_truth_BGRA, cv2.COLOR_BGRA2RGB)

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(fruit_RGB)
plt.axis('off')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(ground_truth_RGB)
plt.axis('off')
plt.title('Ground Truth')

plt.subplot(1, 3, 3)
plt.imshow(fruit_gray, cmap='gray')
plt.axis('off')
plt.title('Fruit in GrayScale')
plt.show()

# Otsu's Method
# Calculate the Otsu's Threshold
threshold_otsu, result_otsu = cv2.threshold(fruit_gray, 0, 255, cv2.THRESH_OTSU)
print("Obtained Threshold: ", threshold_otsu)
result_otsu_RGB = cv2.cvtColor(result_otsu, cv2.COLOR_GRAY2RGB)

# Final Image
plt.figure()
plt.imshow(result_otsu_RGB)
plt.axis('off')
plt.title("Thresholded with Otsu's Method")
plt.show()

# Metric
SNR_otsu = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result_otsu_RGB)
print("The peak signal to noise ratio, for Otsu's method, is:", SNR_otsu)


# Color Segmentation
fruit_HSV = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2HSV)

# HSV ranges between (0-180, 0-255, 0-255)
maxi = 0
max_i = -1
for i in range(0, 180, 10):
    light = (i, 0, 20)
    dark = (i+10, 255, 255)
    mask = cv2.inRange(fruit_HSV, light, dark)
    result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)
    SNR = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result)
    if SNR > maxi:
        max_i = i
    print("The peak signal to noise ratio, for H =", i, "is: ", SNR)

light = (max_i, 0, 20)
dark = (max_i+10, 255, 255)
mask = cv2.inRange(fruit_HSV, light, dark)
result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

plt.figure()
plt.imshow(result)
plt.title('Segmentation using Color Masking')
plt.axis('off')
plt.show()


# If I choose the values of H near to 0-10 and 170-180, all the image is represented
light = (0, 0, 20)
dark = (10, 255, 255)
mask = cv2.inRange(fruit_HSV, light, dark)
result1 = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

light = (170, 0, 20)
dark = (180, 255, 255)
mask = cv2.inRange(fruit_HSV, light, dark)
result2 = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

result = cv2.add(result1, result2)

SNR = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result)
print("In the second case, the peak signal to noise ratio, for H is: ", SNR)

plt.figure()
plt.imshow(result)
plt.title('Segmentation using Color Masking, but manually')
plt.axis('off')
plt.show()


# K-Means
twoDimage = fruit_RGB.reshape((-1, 3))
twoDimage = np.float32(twoDimage)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
attempts = 10
K = 10

ret, label, center = cv2.kmeans(twoDimage, K, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape(fruit_RGB.shape)

plt.figure()
plt.imshow(result_image)
plt.axis('off')
plt.title('Segmented Image with K-Means')
plt.show()


# Contour Detection
ret, thresh = cv2.threshold(fruit_gray, 150, 255, cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh, cmap='gray')
plt.axis('off')
plt.title('Binary image')
plt.show()

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

image_copy = fruit_RGB.copy()
cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)

plt.figure()
plt.imshow(image_copy)
plt.axis('off')
plt.title('Original image with Contours')
plt.show()

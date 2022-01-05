import matplotlib.pyplot as plt
import cv2
import skimage
from skimage.metrics import peak_signal_noise_ratio

fruit_BGR = cv2.imread('./image/goiaba-43.jpg')
fruit_RGB = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2RGB)
fruit_gray = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2GRAY)
fruit_HSV = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2HSV)

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


# Automatically
# HSV ranges between (0-180, 0-255, 0-255)
maxi = 0
maxi_i = -1
for i in range(0, 180, 10):
    light = (i, 0, 20)
    dark = (i+10, 255, 255)
    mask = cv2.inRange(fruit_HSV, light, dark)
    result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)
    SNR = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result)
    if SNR > maxi:
        maxi_i = i
    print("The peak signal to noise ratio, for H =", i, "is: ", SNR)

light = (maxi_i, 0, 20)
dark = (maxi_i+10, 255, 255)
mask = cv2.inRange(fruit_HSV, light, dark)
result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(ground_truth_RGB)
plt.title('Ground Truth')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(result)
plt.title('Segmentation using color masking')
plt.show()

# Manually
# If I choose the values of H near to 0-10 and 170-180, all the image is represented
light = (0, 0, 0)
dark = (10, 255, 255)
mask1 = cv2.inRange(fruit_HSV, light, dark)

light = (170, 0, 0)
dark = (180, 255, 255)
mask2 = cv2.inRange(fruit_HSV, light, dark)

light = (0, 0, 0)
dark = (180, 65, 255)
mask3 = cv2.inRange(fruit_HSV, light, dark)

mask = mask1 + mask2 + mask3
result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

SNR = skimage.metrics.peak_signal_noise_ratio(ground_truth_RGB, result)
print("In the second case, the peak signal to noise ratio, for H is: ", SNR)

plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(ground_truth_RGB)
plt.title('Ground Truth')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(result)
plt.title('Segmentation using color masking, but manually')
plt.axis('off')
plt.show()

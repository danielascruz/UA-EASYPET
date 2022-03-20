import matplotlib.pyplot as plt
import cv2

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

import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.colors import hsv_to_rgb

#  OpenCV by default reads images in BGR format (switch blue channels with the red ones)
fruit_BGR = cv2.imread('./image/fruta-1024x676.jpg')
plt.imshow(fruit_BGR)
plt.axis('off')
plt.show()

# Original Image
fruit_RGB = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2RGB)
plt.imshow(fruit_RGB)
plt.axis('off')
plt.title('Original Image')
plt.show()

# Use this to pick a color: https://imagecolorpicker.com/
# Use this to convert RGB to HSV: https://www.rapidtables.com/convert/color/rgb-to-hsv.html
fruit_HSV = cv2.cvtColor(fruit_RGB, cv2.COLOR_RGB2HSV)


dark = (80, 223, 221)
light = (110, 46, 246)

lo_square = np.full((10, 10, 3), light, dtype=np.uint8) / 255.0
do_square = np.full((10, 10, 3), dark, dtype=np.uint8) / 255.0
plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show()


mask = cv2.inRange(fruit_HSV, dark, light)

# Impose the mask on top of the original image
result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()

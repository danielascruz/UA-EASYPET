import matplotlib.pyplot as plt
import cv2


#  OpenCV by default reads images in BGR format (switch blue channels with the red ones)
fruit_BGR = cv2.imread('./image/fruta-1024x676.jpg')

# Original Image
fruit_RGB = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2RGB)
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(fruit_RGB)
plt.axis('off')
plt.title('Original Image')

# Use this to pick a color: https://imagecolorpicker.com/
# Use this to convert RGB to HSV: https://www.rapidtables.com/convert/color/rgb-to-hsv.html
fruit_HSV = cv2.cvtColor(fruit_RGB, cv2.COLOR_RGB2HSV)

# (H, S, V)
light = (170, 50, 20)
dark = (180, 250, 255)
mask = cv2.inRange(fruit_HSV, light, dark)

# Impose the mask on top of the original image
result = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

plt.subplot(1, 2, 2)
plt.imshow(result)
plt.title('Color Segmentation with OpenCV')
plt.axis('off')
plt.show()

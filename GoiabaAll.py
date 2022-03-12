import matplotlib.pyplot as plt
import numpy as np
import cv2


fruit_BGR = cv2.imread('./image/goiaba-43.jpg')
fruit_RGB = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2RGB)
fruit_gray = cv2.cvtColor(fruit_BGR, cv2.COLOR_BGR2GRAY)

# Circular mask to apply in original image and isolate the object
mask = np.zeros(fruit_RGB.shape[:2], dtype="uint8")  # All zeros -> zero is black/ .shape[:2] to get dimensions of image
cv2.circle(mask, (206, 197), 74, 255, -1)
cv2.circle(mask, (352, 206), 76, 255, -1)
ground_truth = cv2.bitwise_and(fruit_RGB, fruit_RGB, mask=mask)

plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(fruit_RGB)
plt.axis('off')
plt.title('Original Image')

plt.subplot(2, 1, 2)
plt.imshow(ground_truth)
plt.axis('off')
plt.title('Ground Truth')


# K-Means
twoDimage = fruit_RGB.reshape((-1, 3))
twoDimage = np.float32(twoDimage)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
attempts = 10
K = 15

ret, label, center = cv2.kmeans(twoDimage, K, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
Kmeans_result = res.reshape(fruit_RGB.shape)

plt.figure()
plt.imshow(Kmeans_result)
plt.axis('off')
plt.title('Segmented Image with K-Means')


# Segmentation by color of K-means result
Kmeans_result_HSV = cv2.cvtColor(Kmeans_result, cv2.COLOR_RGB2HSV)

n_divisoes_y = 5
n_divisoes_x = 10
iou_score_total = np.zeros((int(180/n_divisoes_x), int(255/n_divisoes_y)))
for i in range(0, 180, n_divisoes_x):
    for j in range(0, 255, n_divisoes_y):
        light = (i, j, 0)
        dark = (i+n_divisoes_x, j+n_divisoes_y, 255)
        mask = cv2.inRange(Kmeans_result_HSV, light, dark)
        color_result = cv2.bitwise_and(Kmeans_result, Kmeans_result, mask=mask)
        intersection = np.logical_and(ground_truth, color_result)
        union = np.logical_or(ground_truth, color_result)
        iou_score = (np.sum(intersection) / np.sum(union)) * 100
        iou_score_total[int(i/n_divisoes_x), int(j/n_divisoes_y)] = iou_score

plt.figure()
plt.imshow(iou_score_total)


linha_H = np.arange(0, 180, n_divisoes_x)
matriz_H = np.vstack([linha_H]*iou_score_total.shape[1])
matriz_H = matriz_H.T

coluna_S = np.arange(0, 255, n_divisoes_y)
matriz_S = np.vstack([coluna_S]*iou_score_total.shape[0])
matriz_S = matriz_S

matriz_H = matriz_H[iou_score_total > 0.1*iou_score_total.max()]
matriz_S = matriz_S[iou_score_total > 0.1*iou_score_total.max()]

for x in range(0, Kmeans_result_HSV.shape[0]):
    for y in range(0, Kmeans_result_HSV.shape[1]):
        index = np.where(matriz_H[(matriz_H > Kmeans_result_HSV[x, y, 0]) & (matriz_S > Kmeans_result_HSV[x, y, 0])])

        if len(index[0]) == 0:
            Kmeans_result_HSV[x, y, 0] = 0
            Kmeans_result_HSV[x, y, 1] = 0
            Kmeans_result_HSV[x, y, 2] = 0
        # print(len(index[0]))

result = cv2.cvtColor(Kmeans_result_HSV, cv2.COLOR_HSV2RGB)
plt.figure()
plt.imshow(result)

mask = []
for i in result:cd
    line = []
    for j in i:
        if j[0] != 0 or j[1] != 0 or j[2] != 0:
            line.append([255, 255, 255])
        else:
            line.append([0, 0, 0])
    mask.append(line)

plt.figure()
plt.imshow(mask)
plt.show()

import numpy as np
from skimage import data
import matplotlib.pyplot as plt

camera = data.camera()
camera[:10] = 0  # todas as 10 primeiras linhas e colunas ficam com valor zero

mask = camera < 87  # filtra. Tudo o que é abaixo de 87 fica True
camera[mask] = 255  # torna os True em 255

inds_x = np.arange(len(camera))  # range, igualmente espaçado até length da camera
inds_y = (4 * inds_x) % len(camera)
camera[inds_x, inds_y] = 0

l_x, l_y = camera.shape[0], camera.shape[1]    # shape the array
X, Y = np.ogrid[:l_x, :l_y]   # novos eixos

outer_disk_mask = (X - l_x / 2)**2 + (Y - l_y / 2)**2 > (l_x / 2)**2
camera[outer_disk_mask] = 0

plt.figure(figsize=(4, 4))

plt.imshow(data.camera(), cmap='gray')
plt.axis('off')
plt.show()

plt.imshow(camera, cmap='gray')
plt.axis('off')
plt.show()

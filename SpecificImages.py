import matplotlib.pyplot as plt
import matplotlib

from skimage import data

matplotlib.rcParams['font.size'] = 18

# Stereo images
fig, axes = plt.subplots(1, 2, figsize=(8, 4))  # n.linhas, n.colunas,
ax = axes.ravel()  # transforma os eixos num array de 1D

images = data.stereo_motorcycle()  # Tem 3 linhas de informação
ax[0].imshow(images[0])  # No primeiro eixo, temos os dados referentes à 1 imagem
ax[1].imshow(images[1])

fig.tight_layout()  # ajusta o gráfico ao que aparece
plt.show()

# PIV images
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

images = data.vortex()
ax[0].imshow(images[0])
ax[1].imshow(images[1])

plt.figure()
fig.tight_layout()
plt.show()

# Faces and non-faces
fig, axes = plt.subplots(4, 5, figsize=(20, 20))
ax = axes.ravel()

images = data.lfw_subset()
for i in range(20):
    ax[i].imshow(images[90+i], cmap=plt.cm.gray)
    ax[i].axis('off')   # Turn off axis lines and labels.

fig.tight_layout()
plt.show()

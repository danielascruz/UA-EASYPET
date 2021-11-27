# General-purpose image
import matplotlib.pyplot as plt
import matplotlib

from skimage import data
# from skimage.color import rgb2gray

matplotlib.rcParams['font.size'] = 18   # customize matplotlib

images = ('astronaut',
          'binary_blobs',
          'brick',
          'colorwheel',
          'camera',
          'cat',
          'checkerboard',
          'clock',
          'coffee',
          'coins',
          'eagle',
          'grass',
          'gravel',
          'horse',
          'logo',
          'page',
          'text',
          'rocket',
          )

for name in images:
    caller = getattr(data, name)   # Get's a certain image from the data examples
    image = caller()
    plt.figure()
    plt.title(name)
    if image.ndim == 2:   # se for monocromático (2 dimensoes)
        plt.imshow(image, cmap=plt.cm.gray)  # cmap = Color map; tons de cinza
    else:
        plt.imshow(image)

plt.show()

    # Se eu quiser mostrar as imagens todas a preto
    # if image.ndim == 3:   # as que estão em RGB
        # image1 = rgb2gray(image)
        # plt.imshow(image1, cmap=plt.cm.gray)  # passei de rgb para gray, e agora tenho o colormap a indicar para ser preto
    # else:   # já estavam na gray scale
        # plt.imshow(image,cmap=plt.cm.gray)




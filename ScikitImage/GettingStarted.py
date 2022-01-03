# Getting Started
from skimage import data, io, filters

image = data.camera()  # get the data related to 'coins'
edges = filters.sobel(image)  # find the edges in an image (type of filter of skimage)
io.imshow(edges)  # define the type of chart / show only the edges
io.show()   # show the image

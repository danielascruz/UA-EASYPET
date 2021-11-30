# define the vertical filter
vertical_filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

# define the horizontal filter
horizontal_filter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

# get the dimensions of the image
n, m, d = image.shape

# initialize the edges image
edges_img = image.copy()

# loop over all pixels in the image
for row in range(3, n - 2):
    for col in range(3, m - 2):
        # create little local 3x3 box
        local_pixels = image[row - 1:row + 2, col - 1:col + 2, 0]

        # apply the vertical filter
        vertical_transformed_pixels = vertical_filter * local_pixels
        # remap the vertical score
        vertical_score = vertical_transformed_pixels.sum() / 4

        # apply the horizontal filter
        horizontal_transformed_pixels = horizontal_filter * local_pixels
        # remap the horizontal score
        horizontal_score = horizontal_transformed_pixels.sum() / 4

        # combine the horizontal and vertical scores into a total edge score
        edge_score = (vertical_score ** 2 + horizontal_score ** 2) ** .5

        # insert this edge score into the edges image
        edges_img[row, col] = [edge_score] * 3

# remap the values in the 0-1 range in case they went out of bounds
edges_img = edges_img / edges_img.max()

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

axes[0].imshow(image)
axes[0].set_title("Original")
axes[0].set_axis_off()

axes[1].imshow(edges_img)
axes[1].set_title("Edges")
axes[1].set_axis_off()

fig.tight_layout()
plt.show()
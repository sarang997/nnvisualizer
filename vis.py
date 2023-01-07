import h5py
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Open the H5 file
path = '/home/sarang/Downloads/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
f = h5py.File(path, 'r')

# Set the number of rows and columns for the plot grid
n_rows = 4
n_cols = 4

# Set the figure size
plt.figure(figsize=(n_cols*4, n_rows*4))

# Loop through the groups in the file
for i, group in enumerate(f.keys()):
  # Loop through the datasets in the group
    for j, dataset in enumerate(f[group].keys()):
    # Get the weights for the dataset
        arr = f[group][dataset][()]
        # print(type(weights),weights.shape)

        # Reshape the array to a 2D array
        arr = arr.reshape(3*3, 3*64)

        # Plot the array as an image
        plt.imshow(arr)

        # Show the plot
        plt.show()
        exit()
        img = Image.fromarray(weights.astype('uint8'), 'RGB')
        img.save('image.png')
        img.show()

    # # Flatten the weights to 1D array
    #     weights = weights.flatten()

    #     # Create a subplot for the dataset
    #     # plt.subplot(n_rows, n_cols, i*n_cols + j + 1)

    #     # Create a histogram of the weights
    #     plt.hist(weights)
    #     plt.title(f'{group}:{dataset}')

# Adjust the spacing between subplots
# plt.tight_layout()

# # Show the plot
# plt.show()

# # Close the file
# f.close()

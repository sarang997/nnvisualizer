import matplotlib.plt as pyplot

class Visualize:
    def __init__(self,weights_single_layer):
        self.arr = weights_single_layer
        print('constructor function')

    def plot_np_ndarray(self):
        arr = arr.reshape(3*3, 3*64)

        # Plot the array as an image
        plt.imshow(arr)

        # Show the plot
        plt.show()
        exit()
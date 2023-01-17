
from nnvisualizer.Setup import Setup
from nnvisualizer.Utils import Utils
import numpy as np

#Setting up the model before visualizing
#
path = '/home/sarang/Downloads/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
setup = Setup(model_path =path)
setup.showPlot()

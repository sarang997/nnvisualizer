
from nnvisualizer.Setup import Setup
from nnvisualizer.Utils import Utils

#Setting up the model before visualizing
#
path = '/home/sarang/Downloads/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
setup = Setup(model_path =path)
model = setup.loadModel() 
info = setup.modelInfo()
print(info)
f1 = model['block1_conv1']
f2 = f1.items()
print(f2)
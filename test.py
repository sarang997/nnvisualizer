
from nnvisualizer.Setup import Setup
from nnvisualizer.Utils import Utils

#Setting up the model before visualizing
setup = Setup(model_path ="this_is_the_model_path")
setup.loadModel() 
setup.modelInfo()
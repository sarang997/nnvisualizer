#this class is used to load the ML model and is the first entry for using the library
from nnvisualizer.Utils import Utils
from nnvisualizer.Visualize import Visualize

import h5py

class Setup():
    def __init__(self,model_path):
        self.model_path = model_path
        # file = h5py.File(self.model_path, 'r')


    #function to load the model returns the .h5 model file
    def loadModel(self):
        file = h5py.File(self.model_path, 'r')
        return file

    def modelInfo(self):
        print('========MODEL INFO========')
        file = self.loadModel()
        layers = list(file.keys())
        totalLayers= len(layers)
        info = {
            'layers':layers,
            'totalLayers':totalLayers
               }
        print('========MODEL INFO========')
        return info


    def totalLayers(self):
        return 1
    
    def getWeights(self):
        f = h5py.File(self.model_path, 'r')
        # Loop through the groups in the file
        for i, group in enumerate(f.keys()):
        # Loop through the datasets in the group
            for j, dataset in enumerate(f[group].keys()):
                # Get the weights for the dataset
                weights = f[group][dataset][()]
                return weights
                exit('dfjdjf')
    
    def showPlot(self):
        arr = self.getWeights()
        Visualize.plot_np_ndarray(arr)
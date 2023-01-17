#this class is used to load the ML model and is the first entry for using the library
from nnvisualizer.Utils import Utils
from nnvisualizer.Visualize import Visualize

import h5py

class Setup():
    def __init__(self,model_path):
        self.model_path = model_path


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
        all_weights = []
        for i, group in enumerate(f.keys()):
        # Loop through the datasets in the group
            layer_weights = []
            for j, dataset in enumerate(f[group].keys()):
                # Get the weights for the dataset
                weights = f[group][dataset][()]
                layer_weights.append(weights)
            all_weights.append(layer_weights)
        return all_weights
    
    def showPlot(self):
        arr = self.getWeights()
        for layer in arr:
            print(len(layer))
            for dataset in layer:
                visualize = Visualize(dataset)
                self.dataset = dataset
                try:
                    visualize.plot_np_ndarray()
                except:
                    continue
                # exit('dfjdfj')
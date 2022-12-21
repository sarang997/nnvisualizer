#this class is used to load the ML model and is the first entry for using the library
from nnvisualizer.Utils import Utils
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
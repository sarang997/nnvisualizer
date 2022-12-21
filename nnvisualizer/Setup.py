#this class is used to load the ML model and is the first entry for using the library
from nnvisualizer.Utils import Utils
import h5py

class Setup():
    def __init__(self,model_path):
        self.model_path = model_path
        # file = h5py.File(self.model_path, 'r')


    #function to load the model returns the .h5 model file
    def loadModel(self):
        print('model loader function')  
        file = h5py.File(self.model_path, 'r')
        return file
    
    def modelInfo(self):
        path = self.model_path
        layers = self.totalLayers()
        print("path: "+ path,"layers: "+str(layers))

    def totalLayers(self):
        return 1
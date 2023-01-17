#this class has utility functions that can be used on the model after loading

class Utils:
    def __init__(self,setup):

        self.setup = setup
    
    #gives the info about the model/things like number of layers    
    def modelInfo(self):
        self.setup.modelPath()
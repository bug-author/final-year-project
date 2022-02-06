import numpy as np

class VectorNormalizer:
    def __init__(self):
        self.norm = []
        
    def fit(self, dataframe):
        self.norm = np.linalg.norm(dataframe, axis=0)
        return self.norm
    
    def transform(self, dataframe):
        if len(self.norm) > 0:
            return dataframe/self.norm
    
    def inverse_transform(self, dataframe):
        if len(self.norm) > 0:
            return dataframe*self.norm
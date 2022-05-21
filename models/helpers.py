
import numpy as np


class VectorNormalizer:
    def __init__(self):
        self.norm = None

    def fit(self, dataframe):
        self.norm = np.linalg.norm(dataframe, axis=0)
        return self.norm

    def transform(self, dataframe):
        if self.norm is not None:
            return dataframe/self.norm

    def inverse_transform(self, dataframe, norms=None):
        if norms is not None:
            return dataframe*norms
        if self.norm is not None:
            return dataframe*self.norm

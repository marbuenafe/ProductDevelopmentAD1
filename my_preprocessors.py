import pandas as pd
import numpy as np
import datetime
from sklearn.base import BaseEstimator, TransformerMixin

class Mapper(BaseEstimator, TransformerMixin):
    #Constructor
    def __init__(self, variables, mappings):
        if not isinstance(variables, list):
            raise ValueError("Las variables debe ser incluida en una lista.")
        #campos de clas Mapper
        self.variables = variables
        self.mappings = mappings
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X=X.copy()
        for variable in self.variables:
            X[variable]=X[variable].map(self.mappings)
        return X
    

import pandas as pd
import numpy as np
import datetime
from sklearn.base import BaseEstimator, TransformerMixin

#Clase para manejo de variables temporales en el modelo de House Price
class TremporalVariableTransformer(BaseEstimator, TransformerMixin):

    #Constructor
    def __init__(self, variables, reference_variable):
        if not isinstance(variables, list):
            raise ValueError("La varible debe ser incluida en una lista.")
        
        self.variables = variables
        self.reference_variable = reference_variable

    #metodo fit para habilitar metodo transform
    def fit(self, X, y=None):
        return self

    #metodo para transformar variables temporales.
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[self.reference_variable] - X[feature]
        return X

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
    
class TotalProducto(variables):
    
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()

    #def __init__(self, variables):
    #    if not isinstance(variables, list):
    #        raise ValueError("Las variables debe ser incluida en una lista.")
    #    #campos de clas Mapper
    #    self.variables = variables
    
    #def fit(self, X, y=None):
    #    return self
    
    #def transform(self, X):
    #    X=X.copy()
       
    #    for var in self.variables:
    #        X[varAnt] = X[var]
    #        X[var]=X[var]+X[varAnt]
        return X 
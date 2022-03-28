# Librerias
import joblib as jl
import config as cfg
import pandas as pd
import numpy as np

# Cargamos modelo y pipeline
marketing_model = jl.load('housePrice_pipeline.pkl')

def predict(X):        
        X = X[cfg.FEATURES]
        predicts = marketing_model.predict(X)
        result = predicts
        return result
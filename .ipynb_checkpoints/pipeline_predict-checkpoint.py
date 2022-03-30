import joblib
import pandas as pd
import numpy as np
import config as cfg

X_test = pd.read_csv("Marqueting.csv", encoding='latin-1')
X_test = X_test[cfg.FEATURES]

# Cargamos modelo y pipeline
house_predic_model = joblib.load('housePrice_pipeline.pkl')

def predict(X):        
        predicts = house_predic_model.predict(X)
        result = predicts
        print(result)

predict(X_test)
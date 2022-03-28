from flask import Flask, jsonify, request
from itsdangerous import json

import json
import pandas as pd
import script as pp

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return jsonify(username="Maria Reyes", email="maria@gmail.com",id=3456)

@app.route("/predecir", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    json_data = json.dumps(json_data)
    json_data = json.loads(json_data)

    dataframe = pd.DataFrame.from_dict(json_data, orient="index")
    resultado = pp.predict(dataframe.T)
    return jsonify({"Prediccion":resultado[0]})
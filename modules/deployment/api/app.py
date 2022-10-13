# PSEUDOCODE!
# Requires the pip-installable DS and MLE modules...
from flask import Flask, request
import pandas as pd
from data_science.modelling import SimpleModel

MODEL = SimpleModel()
MODEL.load('/models')

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    print(request)
    data = request.json
    print(data)

    label = MODEL.predict_with_logging(
        data["idx"],
        pd.DataFrame([data["features"]])
    )

    return {"label": int(label)}

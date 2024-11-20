import pickle
import numpy as np

class InferenceModel:
    def __init__(self, model_path="./src/model/isolation_forest_model.pkl"):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, data):
        predictions = self.model.predict(np.array(data))
        return predictions.tolist()

from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Load your model
model_path = "./src/model/isolation_forest_model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    # Display a simple form to input data
    return render_template('index.html')

@app.route('/invocations', methods=['POST'])
def invoke_model():
    # Get data from the form
    input_data = request.form['data']
    
    # Convert the input data to a numpy array
    data_array = np.array([list(map(float, input_data.split(',')))])
    
    # Make predictions with the model
    prediction = model.predict(data_array)
    
    # Return the prediction as a JSON response
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

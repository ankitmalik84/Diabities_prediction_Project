from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

# Load the trained model
model = joblib.load('diabetes_model.pkl')

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def home():
    return "Welcome to the Diabetes Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json(force=True)
    
    # Convert data into numpy array and reshape for the model
    input_data = np.array([data['features']])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the result as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)

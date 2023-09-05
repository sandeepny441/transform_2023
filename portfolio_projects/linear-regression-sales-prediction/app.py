from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])



def predict():
    data = request.json  # Get JSON data from frontend
    month = np.array([[data['month']]])  # Create a numpy array from the input
    prediction = model.predict(month)[0]  # Get prediction from model
    return jsonify({'prediction': prediction})  # Return the prediction as JSON

if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, request, jsonify, send_from_directory
import joblib
import numpy as np

app = Flask(__name__, static_folder='static')

# Paths to the model and scaler
model_path = '/Users/srinivasareddypadala/Desktop/hackathon final 2 /Credit_Risk_Analysis_for_extending_Bank_Loans.pkl'
scaler_path = '/Users/srinivasareddypadala/Desktop/hackathon final 2 /RobustScaler.pkl'

# Load the pre-trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract features from the request data
        features = [
            data['age'],
            data['education'],
            data['employed'],
            data['address'],
            data['income'],
            data['debtincome'],
            data['creddebt'],
            data['otherdebt']
        ]

        # Convert features to numpy array
        features = np.array([features])

        # Scale the features using the loaded scaler
        features_scaled = scaler.transform(features)

        # Predict using the loaded model
        prediction = model.predict(features_scaled)

        # Return prediction result
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})






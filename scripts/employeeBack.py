from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import joblib
import os
import numpy as np
import pandas as pd

# Step 1: Set up Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Paths for the models folder relative to this script
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))
MODEL_PATH = os.path.join(BASE_DIR, "employee_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "employee_scaler.pkl")
ENCODERS_PATH = os.path.join(BASE_DIR, "employee_label_encoders.pkl")

# Step 2: Load the employee model, scaler, and encoders
if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH) or not os.path.exists(ENCODERS_PATH):
    raise FileNotFoundError("Model, scaler, or encoders not found. Ensure they are saved correctly in the 'models' directory.")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoders = joblib.load(ENCODERS_PATH)

# Step 3: Define employee features and helper function
employee_features = ['self_employed', 'work_interfere', 'remote_work', 
                     'family_history', 'benefits', 'leave', 'care_options', 'treatment']

engineered_features = ['policy_support_score', 'self_employed_remote_work', 
                       'mental_health_history_score', 'remote_work_leave_ratio', 
                       'benefits_leave_interaction', 'care_options_work_interaction']

def preprocess_input(data):
    """
    Preprocess input data: encode categorical features, engineer new features, and scale.

    Args:
        data (dict): Input feature values in JSON format.

    Returns:
        numpy.ndarray: Preprocessed and scaled feature values ready for model prediction.
    """
    # Apply label encoding
    for col in employee_features:
        if col in label_encoders:
            if col in data:
                data[col] = label_encoders[col].transform([data[col]])[0]
            else:
                raise ValueError(f"Missing required field: {col}")
    
    # Convert to DataFrame
    input_df = pd.DataFrame([data], columns=employee_features)
    
    # Feature engineering
    input_df['policy_support_score'] = input_df[['benefits', 'care_options', 'leave']].sum(axis=1)
    input_df['self_employed_remote_work'] = input_df['self_employed'] * input_df['remote_work']
    input_df['mental_health_history_score'] = input_df[['family_history']].sum(axis=1)
    input_df['remote_work_leave_ratio'] = input_df['remote_work'] / (input_df['leave'] + 1)
    input_df['benefits_leave_interaction'] = input_df['benefits'] * input_df['leave']
    input_df['care_options_work_interaction'] = input_df['care_options'] * input_df['work_interfere']
    
    # Ensure all required features are included
    final_features = employee_features + engineered_features
    input_df = input_df.reindex(columns=final_features, fill_value=0)
    
    # Scale data
    scaled_data = scaler.transform(input_df)
    return scaled_data

@app.route('/')
def home():
    """
    Home endpoint to check if the API is running.

    Returns:
        str: A success message indicating the API is active.
    """
    return "Employee API is running!", 200

# Step 4: Define prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict whether an employee's environment is mental health-friendly.

    Request Body:
        JSON containing values for required features:
        - self_employed, work_interfere, remote_work, family_history, benefits,
          leave, care_options, treatment.

    Returns:
        JSON: A dictionary containing the prediction result or an error message.
    """
    try:
        # Parse input JSON
        input_data = request.json

        # Debug: Print the incoming data from the frontend
        print("Received input data from frontend:", input_data)

        if not input_data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Preprocess input
        processed_data = preprocess_input(input_data)
        
        # Make prediction
        prediction = model.predict(processed_data)
        friendly_score = "Mental Health Friendly" if prediction[0] == 1 else "Not Mental Health Friendly"
        
        return jsonify({"prediction": friendly_score})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Step 5: Run Flask app
if __name__ == "__main__":
    # Start the Flask application on port 5003
    app.run(debug=True, port=5003)

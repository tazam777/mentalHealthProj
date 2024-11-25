from flask import Flask, request, jsonify
import joblib
import os
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Paths for the models folder relative to the scripts folder
MODELS_PATH = os.path.join(os.path.dirname(__file__), "../models")

# Load saved model and preprocessing artifacts
model = joblib.load(os.path.join(MODELS_PATH, 'company_model.pkl'))
scaler = joblib.load(os.path.join(MODELS_PATH, 'company_scaler.pkl'))

# Load LabelEncoders for each feature
label_encoders = {
    "benefits": joblib.load(os.path.join(MODELS_PATH, 'benefits_label_encoder.pkl')),
    "wellness_program": joblib.load(os.path.join(MODELS_PATH, 'wellness_program_label_encoder.pkl')),
    "anonymity": joblib.load(os.path.join(MODELS_PATH, 'anonymity_label_encoder.pkl')),
    "leave": joblib.load(os.path.join(MODELS_PATH, 'leave_label_encoder.pkl')),
    "seek_help": joblib.load(os.path.join(MODELS_PATH, 'seek_help_label_encoder.pkl')),
    "remote_work": joblib.load(os.path.join(MODELS_PATH, 'remote_work_label_encoder.pkl')),
    "mental_health_consequence": joblib.load(os.path.join(MODELS_PATH, 'mental_health_consequence_label_encoder.pkl')),
    "supervisor": joblib.load(os.path.join(MODELS_PATH, 'supervisor_label_encoder.pkl')),
}

def handle_unseen_labels(feature, value, encoder):
    """Check if value exists in encoder classes; if not, map it to the most frequent class."""
    if value not in encoder.classes_:
        print(f"Unseen label '{value}' for feature '{feature}', mapping to default.")
        return encoder.transform([encoder.classes_[0]])[0]
    return encoder.transform([value])[0]

# Define route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input
        input_data = request.json
        
        # Extract and encode features
        features = []
        for feature, encoder in label_encoders.items():
            if feature not in input_data:
                return jsonify({"error": f"Missing feature: {feature}"}), 400
            encoded_value = handle_unseen_labels(feature, input_data[feature], encoder)
            features.append(encoded_value)
        
        # Scale features
        features_scaled = scaler.transform([features])
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        prediction_prob = model.predict_proba(features_scaled)[0][1]  # Probability of being 1
        
        # Return response
        return jsonify({
            "mental_health_friendly": bool(prediction),
            "confidence": round(prediction_prob * 100, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
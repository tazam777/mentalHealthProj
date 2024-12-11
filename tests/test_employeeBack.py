import pytest
from flask import json
from scripts.employeeBack import app, preprocess_input

@pytest.fixture
def client():
    """Set up a Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Employee API is running!" in response.data

def test_missing_input(client):
    """Test the /predict endpoint with no input data."""
    response = client.post('/predict', json={})
    assert response.status_code == 400
    assert response.json['error'] == "No input data provided"

def test_missing_required_field(client, mocker):
    """Test the /predict endpoint with missing required fields."""
    input_data = {
        "self_employed": "No",
        "work_interfere": "Sometimes",
        "remote_work": "Yes"
        # Missing other required fields
    }
    
    mocker.patch('scripts.employeeBack.preprocess_input', side_effect=ValueError("Missing required field: benefits"))
    response = client.post('/predict', json=input_data)
    assert response.status_code == 500
    assert "Missing required field: benefits" in response.json['error']

def test_successful_prediction(client, mocker):
    """Test the /predict endpoint with valid input."""
    input_data = {
        "self_employed": "No",
        "work_interfere": "Sometimes",
        "remote_work": "Yes",
        "family_history": "Yes",
        "benefits": "Yes",
        "leave": "Sometimes",
        "care_options": "Yes",
        "treatment": "Yes"
    }

    # Mock preprocess_input and model.predict
    mocker.patch('scripts.employeeBack.preprocess_input', return_value=[[0, 1, 0, 1, 1, 2, 1, 1, 3, 1]])
    mock_model = mocker.patch('scripts.employeeBack.model.predict', return_value=[1])
    response = client.post('/predict', json=input_data)
    
    assert response.status_code == 200
    assert response.json['prediction'] == "Mental Health Friendly"
    mock_model.assert_called_once()

def test_unseen_labels(client, mocker):
    """Test the /predict endpoint with unseen labels."""
    input_data = {
        "self_employed": "Maybe",  # Unseen label
        "work_interfere": "Sometimes",
        "remote_work": "Yes",
        "family_history": "Yes",
        "benefits": "Unknown",
        "leave": "Rarely",
        "care_options": "No",
        "treatment": "Yes"
    }

    # Mock preprocess_input to handle unseen labels
    mocker.patch('scripts.employeeBack.preprocess_input', return_value=[[0, 1, 0, 1, 1, 2, 1, 1, 3, 1]])
    mock_model = mocker.patch('scripts.employeeBack.model.predict', return_value=[0])
    response = client.post('/predict', json=input_data)

    assert response.status_code == 200
    assert response.json['prediction'] == "Not Mental Health Friendly"
    mock_model.assert_called_once()

def test_internal_server_error(client, mocker):
    """Test the /predict endpoint when an internal server error occurs."""
    input_data = {
        "self_employed": "No",
        "work_interfere": "Sometimes",
        "remote_work": "Yes",
        "family_history": "Yes",
        "benefits": "Yes",
        "leave": "Sometimes",
        "care_options": "Yes",
        "treatment": "Yes"
    }

    # Mock preprocess_input to raise an exception
    mocker.patch('scripts.employeeBack.preprocess_input', side_effect=Exception("Test error"))
    response = client.post('/predict', json=input_data)
    assert response.status_code == 500
    assert "Test error" in response.json['error']

import pytest
import json
from scripts.companyBack import app, handle_unseen_labels

@pytest.fixture
def client():
    """Fixture to set up the Flask test client."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Company API is running!"


def test_missing_input(client):
    """Test the /predict endpoint with no input."""
    response = client.post("/predict", json={})
    assert response.status_code == 400
    assert "No input data provided" in response.json["error"]


def test_missing_feature(client):
    """Test the /predict endpoint with missing required fields."""
    input_data = {
        "benefits": "Yes",
        "wellness_program": "Yes"
        # Missing other required fields
    }
    response = client.post("/predict", json=input_data)
    assert response.status_code == 400
    assert "Missing feature" in response.json["error"]


def test_unseen_labels(client, mocker):
    """Test the /predict endpoint with unseen labels."""
    input_data = {
        "benefits": "Unknown",  # An unseen label
        "wellness_program": "Yes",
        "anonymity": "Yes",
        "leave": "Very easy",
        "seek_help": "No",
        "remote_work": "Yes",
        "mental_health_consequence": "Somewhat",
        "supervisor": "No"
    }

    # Mock the label encoder to simulate unseen label handling
    mocker.patch(
        "scripts.companyBack.handle_unseen_labels",
        side_effect=lambda feature, value, encoder: 0  # Map all unseen labels to 0
    )

    response = client.post("/predict", json=input_data)
    assert response.status_code == 200
    assert "mental_health_friendly" in response.json

def test_successful_prediction(client):
    """Test the /predict endpoint with valid input."""
    input_data = {
        "benefits": "Yes",
        "wellness_program": "Yes",
        "anonymity": "Yes",
        "leave": "Very easy",
        "seek_help": "No",
        "remote_work": "Yes",
        "mental_health_consequence": "Somewhat",
        "supervisor": "No"
    }
    response = client.post("/predict", json=input_data)
    assert response.status_code == 200
    assert "mental_health_friendly" in response.json
    assert "confidence" in response.json

def test_internal_server_error(client, mocker):
    """Test the /predict endpoint with an internal server error."""
    input_data = {
        "benefits": "Yes",
        "wellness_program": "Yes",
        "anonymity": "Yes",
        "leave": "Very easy",
        "seek_help": "No",
        "remote_work": "Yes",
        "mental_health_consequence": "Somewhat",
        "supervisor": "No"
    }

    # Mock handle_unseen_labels to raise an exception
    mocker.patch("scripts.companyBack.handle_unseen_labels", side_effect=Exception("Test error"))

    response = client.post("/predict", json=input_data)
    assert response.status_code == 500
    assert "Test error" in response.json["error"]

def test_internal_server_error(client, mocker):
    # Mock the model prediction to raise an exception
    mocker.patch("companyBack.model.predict", side_effect=Exception("Test exception"))

    # Make a POST request with valid input
    response = client.post("/predict", json={
        "benefits": "Yes",
        "wellness_program": "No",
        "anonymity": "No",
        "leave": "Somewhat easy",
        "seek_help": "Yes",
        "remote_work": "No",
        "mental_health_consequence": "None",
        "supervisor": "Yes",
    })

    # Assert a 500 status code and error message
    assert response.status_code == 500
    assert response.json == {"error": "Test exception"}

import pytest
import pandas as pd
import pycountry
from scripts.data_loader import load_data, clean_gender, standardize_country

@pytest.fixture
def sample_csv(tmp_path):
    """Fixture to create a sample CSV file for testing."""
    data = {
        'Timestamp': ['2024-11-01 12:34:56', '2024-11-02 13:45:00'],
        'Age': [25, 30],
        'Gender': ['M', 'Female']
    }
    file_path = tmp_path / "sample.csv"
    pd.DataFrame(data).to_csv(file_path, index=False)
    return file_path

def test_load_data(sample_csv):
    """Test that load_data correctly loads a CSV and parses the Timestamp column."""
    df = load_data(sample_csv)
    assert isinstance(df, pd.DataFrame)
    assert 'Timestamp' in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df['Timestamp'])  # Check if 'Timestamp' is datetime type

def test_clean_gender():
    """Test the clean_gender function with various gender inputs."""
    assert clean_gender('M') == 'Male'
    assert clean_gender('female') == 'Female'
    assert clean_gender(' Trans Female ') == 'Trans Female'
    assert clean_gender('non-binary') == 'Non-binary/Other'
    assert clean_gender('queer/she/they') == 'Non-binary/Other'
    assert clean_gender('unknown') == 'Non-binary/Other'  # Unclear/unknown gender should fall into 'Non-binary/Other'

def test_standardize_country():
    """Test the standardize_country function with valid and invalid country inputs."""
    assert standardize_country('United States') == 'United States'
    assert standardize_country('Brasil') == 'Brazil'  # Should now pass with manual mapping
    assert standardize_country('UnknownCountry') == 'UnknownCountry'  # Should return as-is for non-existent names
    assert standardize_country('UK') == 'United Kingdom'  # Test for abbreviation mapping

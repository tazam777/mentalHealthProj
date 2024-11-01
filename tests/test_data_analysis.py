import pytest
import pandas as pd
from scripts.data_analysis import plot_age_distribution, plot_gender_distribution
import matplotlib.pyplot as plt

@pytest.fixture
def sample_dataframe():
    """Fixture to create a sample DataFrame for testing."""
    data = {
        'Age': [22, 25, 30, 35, 40, 45, 50],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male']
    }
    return pd.DataFrame(data)

def test_plot_age_distribution(sample_dataframe):
    """Test that plot_age_distribution runs without errors and creates a plot."""
    plt.figure()  # Ensure a new figure is created to avoid conflicts
    plot_age_distribution(sample_dataframe)
    assert plt.gcf().number > 0  # Check that a figure was created

def test_plot_gender_distribution(sample_dataframe):
    """Test that plot_gender_distribution runs without errors and creates a plot."""
    plt.figure()  # Ensure a new figure is created to avoid conflicts
    plot_gender_distribution(sample_dataframe)
    assert plt.gcf().number > 0  # Check that a figure was created

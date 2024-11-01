import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from scripts.model_training import train_model, cross_validate_model

@pytest.fixture
def sample_data():
    """Fixture to create a sample dataset for testing."""
    np.random.seed(42)
    X = pd.DataFrame({
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100),
        'feature3': np.random.randint(0, 2, 100)
    })
    y = pd.Series(np.random.randint(0, 2, 100))
    return X, y

def test_train_model(sample_data):
    """Test the train_model function to ensure it trains without errors and returns expected outputs."""
    X, y = sample_data
    model, X_test, y_test = train_model(X, y)
    
    # Check that the model is trained and returned
    assert isinstance(model, RandomForestClassifier)
    
    # Check that X_test and y_test are returned as DataFrames/Series
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_test, pd.Series)
    
    # Ensure that the test set is not empty
    assert not X_test.empty
    assert not y_test.empty

def test_cross_validate_model(sample_data):
    """Test the cross_validate_model function to ensure it runs and returns cross-validation scores."""
    X, y = sample_data
    cv_scores = cross_validate_model(X, y)
    
    # Check that cross-validation scores are returned as a list/array
    assert isinstance(cv_scores, np.ndarray)
    
    # Check that the number of scores matches the number of folds
    assert len(cv_scores) == 5
    
    # Ensure that the mean score is within a realistic range (0 to 1)
    assert 0 <= cv_scores.mean() <= 1

import pytest
import pandas as pd
from scripts.feature_engineering import encode_features, create_interaction_terms

@pytest.fixture
def sample_dataframe():
    """Fixture to create a sample DataFrame for testing."""
    data = {
        'benefits': ['Yes', 'No', 'Yes', 'No', 'Yes'],
        'care_options': ['Yes', 'No', 'No', 'Yes', 'No'],
        'leave': ['Somewhat easy', 'Very difficult', 'Somewhat easy', 'Don’t know', 'Very easy'],
        'other_col': [1, 2, 3, 4, 5]  # Additional column to ensure non-related columns are ignored
    }
    return pd.DataFrame(data)

def test_encode_features(sample_dataframe):
    """Test encode_features to ensure columns are encoded correctly."""
    columns_to_encode = ['benefits', 'care_options', 'leave']
    df_encoded, label_encoders = encode_features(sample_dataframe, columns_to_encode)

    # Check that the columns are encoded and contain integer values
    for col in columns_to_encode:
        assert pd.api.types.is_integer_dtype(df_encoded[col])

    # Ensure the label encoders are created for each column
    assert len(label_encoders) == len(columns_to_encode)
    assert all(col in label_encoders for col in columns_to_encode)

def test_create_interaction_terms(sample_dataframe):
    """Test create_interaction_terms to ensure the interaction column is created correctly."""
    df_with_interactions = create_interaction_terms(sample_dataframe)

    # Check that the new interaction column exists
    assert 'policy_support_score' in df_with_interactions.columns

    # Validate that the interaction column contains correct summed values
    expected_scores = sample_dataframe.apply(lambda row: (row['benefits'] == 'Yes') +
                                             (row['care_options'] == 'Yes') +
                                             (row['leave'] in ['Somewhat easy', 'Very easy']),
                                             axis=1)
    assert all(df_with_interactions['policy_support_score'] == expected_scores)

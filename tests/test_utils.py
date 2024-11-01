import pytest
import pandas as pd
import numpy as np
from scripts.utils import validate_data, handle_outliers, encode_and_transform

@pytest.fixture
def sample_dataframe():
    """Fixture to create a sample DataFrame for testing."""
    data = {
        'A': [10, 12, 14, 1000, 16],  # Contains an outlier (1000)
        'B': ['cat', 'dog', 'dog', 'cat', 'bird'],
        'C': ['yes', 'no', 'yes', 'no', 'yes']
    }
    return pd.DataFrame(data)

def test_validate_data(sample_dataframe):
    """Test that validate_data correctly validates the presence of required columns."""
    required_columns = ['A', 'B']
    assert validate_data(sample_dataframe, required_columns) == True

    with pytest.raises(ValueError, match="The following required columns are missing:"):
        validate_data(sample_dataframe, ['A', 'B', 'D'])

def test_handle_outliers_iqr(sample_dataframe):
    """Test handle_outliers using the IQR method."""
    df_cleaned = handle_outliers(sample_dataframe, 'A', method='IQR')
    assert df_cleaned['A'].max() < 1000  # Outlier should be removed

def test_handle_outliers_z_score(sample_dataframe):
    """Test handle_outliers using the Z-score method."""
    # Lower the threshold if needed to detect more extreme outliers
    df_cleaned = handle_outliers(sample_dataframe, 'A', method='Z-score', z_score_threshold=1.9)
    assert df_cleaned['A'].max() < 1000, "Outlier was not removed with Z-score method"


# def test_encode_and_transform(sample_dataframe):
#     """Test encode_and_transform for encoding categorical columns."""
#     columns_to_encode = ['B', 'C']
#     df_encoded, label_encoders = encode_and_transform(sample_dataframe, columns_to_encode)

#     assert 'B' in df_encoded.columns
#     assert 'C' in df_encoded.columns
#     assert pd.api.types.is_integer_dtype(df_encoded['B'])
#     assert pd.api.types.is_integer_dtype(df_encoded['C'])

#     # Ensure that label encoders are created
#     assert 'B' in label_encoders
#     assert 'C' in label_encoders

#     # Test using the existing encoders for consistent encoding
#     df_reencoded, _ = encode_and_transform(df_encoded, columns_to_encode, label_encoders=label_encoders)
#     assert df_encoded.equals(df_reencoded)

def test_encode_and_transform(sample_dataframe):
    """Test encode_and_transform for encoding categorical columns."""
    columns_to_encode = ['B', 'C']
    df_encoded, label_encoders = encode_and_transform(sample_dataframe, columns_to_encode)

    assert 'B' in df_encoded.columns
    assert 'C' in df_encoded.columns
    assert pd.api.types.is_integer_dtype(df_encoded['B'])
    assert pd.api.types.is_integer_dtype(df_encoded['C'])

    # Ensure that label encoders are created
    assert 'B' in label_encoders
    assert 'C' in label_encoders

    # Test using the existing encoders for consistent encoding without error
    df_reencoded, _ = encode_and_transform(sample_dataframe, columns_to_encode, label_encoders=label_encoders)
    assert df_encoded.equals(df_reencoded)

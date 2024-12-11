import pandas as pd
import numpy as np

def validate_data(df, required_columns):
    """
    Validate that all required columns are present in the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to validate.
        required_columns (list): List of columns that must be present.
        
    Returns:
        bool: True if all required columns are present, raises an error otherwise.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"The following required columns are missing: {missing_columns}")
    return True

def handle_outliers(df, column, method='IQR', z_score_threshold=3):
    """
    Handle outliers in a DataFrame column using the specified method.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The column in which to handle outliers.
        method (str, optional): The method to use for handling outliers ('IQR' or 'Z-score'). Defaults to 'IQR'.
        z_score_threshold (float, optional): The Z-score threshold for outlier detection. Defaults to 3.
        
    Returns:
        pd.DataFrame: DataFrame with outliers handled in the specified column.
    """
    if method == 'IQR':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    elif method == 'Z-score':
        from scipy import stats
        z_scores = np.abs(stats.zscore(df[column]))
        print(f"Z-scores for column '{column}':\n{z_scores}")
        df = df[z_scores < z_score_threshold]
        return df
    else:
        raise ValueError("Unsupported method. Use 'IQR' or 'Z-score'.")
    
    return df




def encode_and_transform(df, columns, label_encoders=None):
    """
    Encode categorical columns and transform data using provided or new LabelEncoders.
    
    Args:
        df (pd.DataFrame): The DataFrame to encode.
        columns (list): List of column names to encode.
        label_encoders (dict, optional): Existing label encoders to use. If None, new encoders will be created.
        
    Returns:
        pd.DataFrame: The DataFrame with encoded columns.
        dict: Dictionary of LabelEncoders used for encoding.
    """
    from sklearn.preprocessing import LabelEncoder
    
    if label_encoders is None:
        label_encoders = {}
    
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")
        
        # Check if the column is already encoded (numeric)
        if pd.api.types.is_integer_dtype(df[col]):
            continue  # Skip re-encoding already transformed columns
        
        if col not in label_encoders:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
        else:
            le = label_encoders[col]
            df[col] = le.transform(df[col].astype(str))
    
    return df, label_encoders


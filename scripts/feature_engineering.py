from sklearn.preprocessing import LabelEncoder

def encode_features(df, columns):
    """
    Encode categorical features using label encoding.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to encode.
        
    Returns:
        pd.DataFrame: The DataFrame with encoded features.
        dict: Dictionary of LabelEncoders for each column.
    """
    label_encoders = {}
    for col in columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le  # Store encoder for potential reverse mapping or further use
    return df, label_encoders

def create_interaction_terms(df):
    """
    Create a column to summarize policy support based on certain features.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame with an added interaction term.
    """
    df['policy_support_score'] = (
        (df['benefits'] == 'Yes').astype(int) +
        (df['care_options'] == 'Yes').astype(int) +
        (df['leave'].isin(['Somewhat easy', 'Very easy'])).astype(int)
    )
    return df


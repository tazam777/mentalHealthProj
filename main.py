from scripts.data_loader import load_data
from scripts.data_analysis import plot_age_distribution
from scripts.feature_engineering import encode_features, create_interaction_terms
from scripts.model_training import train_model

# Load and clean data
df = load_data('./data/survey.csv')

# Perform analysis
plot_age_distribution(df)

# Specify columns to encode and perform feature encoding
encode_columns = ['benefits', 'care_options', 'leave', 'self_employed', 'treatment']
df, label_encoders = encode_features(df, encode_columns)

# Engineer interaction terms for better feature representation
df = create_interaction_terms(df)

# Ensure you have a target column for training
target_column = 'target_column'  # Replace with your actual target column name

# Check if the target column exists
if target_column not in df.columns:
    raise ValueError(f"Target column '{target_column}' not found in the DataFrame.")

# Train and evaluate the model
X = df.drop(target_column, axis=1)
y = df[target_column]

model, X_test, y_test = train_model(X, y)

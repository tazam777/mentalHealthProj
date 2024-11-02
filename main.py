from scripts.data_loader import load_data, clean_gender, standardize_country
from scripts.data_analysis import (
    plot_age_distribution,
    plot_gender_distribution,
    plot_country_distribution,
    plot_state_distribution,
    plot_self_employment,
    plot_company_size,
    plot_remote_work_status,
    plot_tech_company_status,
    plot_mental_health_benefits,
    plot_care_options_awareness,
    plot_wellness_program,
    plot_negative_consequences,
    plot_coworker_discussion,
    plot_supervisor_discussion,
    plot_interview_discussion,
    plot_medical_leave,
    plot_anonymity_protection,
    plot_seek_help_resources,
    plot_observed_consequences
)
from scripts.feature_engineering import encode_features, create_interaction_terms
from scripts.model_training import train_model
import pandas as pd

# Load and preprocess data
df = load_data('./data/survey.csv')

# Clean and standardize columns
df['Gender'] = df['Gender'].apply(clean_gender)
df['Country'] = df['Country'].apply(standardize_country)

# Plot data visualizations
plot_age_distribution(df)
plot_gender_distribution(df)
plot_country_distribution(df, top_n=10)
plot_state_distribution(df)
plot_self_employment(df)
plot_company_size(df)
plot_remote_work_status(df)
plot_tech_company_status(df)
plot_mental_health_benefits(df)
plot_care_options_awareness(df)
plot_wellness_program(df)
plot_negative_consequences(df)
plot_coworker_discussion(df)
plot_supervisor_discussion(df)
plot_interview_discussion(df)
plot_medical_leave(df)
plot_anonymity_protection(df)
plot_seek_help_resources(df)
plot_observed_consequences(df)

# Encode features and engineer new ones
encode_columns = ['benefits', 'care_options', 'leave', 'self_employed', 'treatment']
df, label_encoders = encode_features(df, encode_columns)
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

print("Script completed successfully!")

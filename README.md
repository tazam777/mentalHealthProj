# Mental Health Survey Data Analysis and Modeling

## Overview
This project is an end-to-end data analysis and modeling pipeline for mental health survey data. It includes data loading, cleaning, exploratory data analysis (EDA), feature engineering, and model training. The goal is to gain insights from the survey data and develop a predictive model that can help assess mental health-friendly environments based on survey responses.

## Project Structure
```plaintext
mental-health-proj/
│
├── data/                     # Data directory (contains survey.csv or other data files)
│
├── scripts/                  # Python modules for different functionalities
│   ├── data_loader.py        # Functions for data loading and preprocessing
│   ├── data_analysis.py      # Functions for data visualization and EDA
│   ├── feature_engineering.py# Functions for feature engineering and encoding
│   ├── model_training.py     # Functions for training and evaluating models
│   └── utils.py              # Utility functions (e.g., data validation, outlier handling)
│
├── tests/                    # Directory for test scripts
│
├── main.py                   # Main script to run the entire pipeline
│
├── environment.yaml          # Conda environment configuration file
│
├── .github/                  # GitHub Actions workflows
│   └── workflows/
│       └── test.yaml         # Workflow for CI/CD (runs tests automatically)
│
└── README.md                 # Project documentation
```

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/project_name.git
    cd project_name
    ```

2. **Create and activate the conda environment**:
    ```bash
    conda env create -f environment.yaml
    conda activate my_project_env
    ```

3. **Install additional dependencies (if any)**:
    ```bash
    pip install -r requirements.txt  # Optional, if more packages are needed
    ```

## Data
Ensure that the `survey.csv` file is placed in the `data/` directory or update the `main.py` script with the correct path.

### Sample Columns in `survey.csv`
- `Age`
- `Gender`
- `Country`
- `self_employed`
- `family_history`
- `treatment`
- `work_interfere`
- ... and more.

## Usage
### Running the Full Pipeline
Execute the main script to run the entire data processing, analysis, and modeling pipeline:
```bash
python main.py
```

### Running Tests
Ensure that `pytest` is installed and run the tests with:
```bash
pytest tests/test_data_analysis.py
```

## Modules Description
### `scripts/data_loader.py`
- **Functions**:
  - `load_data(file_path)`: Loads and preprocesses the data.
  - `clean_gender(gender)`: Cleans and standardizes gender values.
  - `standardize_country(country_name)`: Standardizes country names using the `pycountry` library.

### `scripts/data_analysis.py`
- **Functions for Exploratory Data Analysis**:
  - `plot_age_distribution(df)`: Plots the distribution of age.
  - `plot_gender_distribution(df)`: Plots the distribution of gender.
  - `plot_country_distribution(df, top_n=10)`: Plots the top N countries of respondents.
  - `plot_self_employment(df)`: Plots the distribution of self-employment status.
  - Additional functions for plotting company size, remote work status, mental health benefits, and more.

### `scripts/feature_engineering.py`
- **Functions**:
  - `encode_features(df, columns)`: Encodes categorical features using `LabelEncoder`.
  - `create_interaction_terms(df)`: Creates new features by combining existing columns.

### `scripts/model_training.py`
- **Functions**:
  - `train_model(X, y, model=RandomForestClassifier())`: Trains and evaluates a model with a default `RandomForestClassifier`.
  - `cross_validate_model(X, y, model, cv_folds=5)`: Performs cross-validation on the given model.

### `scripts/utils.py`
- **Functions**:
  - `validate_data(df, required_columns)`: Validates the presence of required columns.
  - `handle_outliers(df, column, method='IQR')`: Handles outliers using IQR or Z-score methods.
  - `encode_and_transform(df, columns, label_encoders=None)`: Encodes and transforms columns with label encoding.

## GitHub Actions
This project includes a GitHub Actions workflow to automatically run tests:
- **Path**: `.github/workflows/test.yaml`
- **Trigger**: Runs on every `push` and `pull_request` to the `main` branch.


### Key Points:
- **Installation**: Provides detailed steps for setting up the project environment.
- **Modules Description**: Outlines the purpose of each module and key functions.
- **Usage**: Guides users on running the pipeline and tests.
- **Future Work**: Mentions potential project improvements.
- **Contributing**: Describes how others can contribute to the project.
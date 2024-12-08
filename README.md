# Mental Health Survey Data Analysis and Prediction Models

## Overview
This project aims to analyze mental health survey data and develop predictive models to assess mental health-friendly environments for companies and employees. The project includes machine learning models, APIs for predictions, and a React-based web application.

## Key Features
- **Machine Learning Models**:
  - **Company Model**: Predicts whether a company is mental health-friendly.
  - **Employee Model**: Predicts mental health-friendliness from the employee's perspective.
- **Web Application**:
  - React-based frontend with navigation for the two models.
  - Flask-based backend APIs for predictions.
- **Integrated Tools**:
  - Input preprocessing using saved scalers and encoders.
  - Seamless communication between frontend and backend with CORS enabled.

## Project Structure
```plaintext
mental-health-proj/
│
├── .github/                  # GitHub workflows
├── data/                     # Dataset storage
│   └── survey.csv
├── frontend/                 # React frontend
│   ├── public/               # Static public files (favicon, manifest, etc.)
│   ├── src/                  # React app source code
│   │   ├── api/              # API call management
│   │   │   └── api.js
│   │   ├── pages/            # React pages
│   │   │   ├── CompanyPage.js
│   │   │   ├── EmployeePage.js
│   │   │   └── LandingPage.js
│   │   ├── App.js            # Main React app component
│   │   ├── index.css         # Global styles
│   │   └── index.js          # Entry point for React app
├── mental-health/            # Python virtual environment
├── models/                   # Saved models and encoders
│   ├── company_model.pkl
│   ├── company_scaler.pkl
│   ├── employee_model.pkl
│   ├── employee_scaler.pkl
│   ├── benefits_label_encoder.pkl
│   ├── anonymity_label_encoder.pkl
│   ├── leave_label_encoder.pkl
│   ├── mental_health_consequence_label_encoder.pkl
│   ├── remote_work_label_encoder.pkl
│   ├── seek_help_label_encoder.pkl
│   ├── supervisor_label_encoder.pkl
│   └── wellness_program_label_encoder.pkl
├── scripts/                  # Backend scripts
│   ├── companyBack.py        # Company Model API
│   ├── employeeBack.py       # Employee Model API
│   ├── data_loader.py        # Data loading utilities
│   ├── data_analysis.py      # Exploratory data analysis
│   ├── feature_engineering.py# Feature engineering utilities
│   ├── model_training.py     # Model training and evaluation
│   └── utils.py              # General utilities
├── tests/                    # Unit tests
│   ├── test_data_analysis.py
│   ├── test_data_loader.py
│   ├── test_feature_engineering.py
│   ├── test_model_training.py
│   └── test_utils.py
├── environment.yaml          # Conda environment configuration
├── main.py                   # Entry point for running the full pipeline
├── mental_health_dataset.csv # Processed dataset
├── model.ipynb               # Jupyter notebook for experimentation
└── README.md                 # Project documentation
```

## Installation

### Backend
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/project_name.git
    cd project_name
    ```

2. **Set up the environment**:
    ```bash
    conda env create -f environment.yaml
    conda activate mental-health
    ```

3. **Install additional dependencies (if any)**:
    ```bash
    pip install -r requirements.txt
    ```

### Frontend
1. Navigate to the `frontend/` directory:
    ```bash
    cd frontend
    ```

2. Install the required dependencies:
    ```bash
    npm install
    ```

## Running the Project

### Backend
1. Navigate to the `scripts/` directory.
2. Start the Flask APIs:
   - Company Model API:
     ```bash
     python companyBack.py
     ```
     Runs on `http://localhost:5002`.
   - Employee Model API:
     ```bash
     python employeeBack.py
     ```
     Runs on `http://localhost:5003`.

### Frontend
1. Navigate to the `frontend/` directory.
2. Start the React app:
    ```bash
    npm start
    ```
   The app will open in your browser at `http://localhost:3000`.

## Usage
1. Open the web app in your browser at `http://localhost:3000`.
2. Use the **Landing Page** to select the Company or Employee prediction model.
3. Enter the required input fields for predictions.
4. Submit the form to receive the prediction and confidence score.

## Contributions
### Git Workflow
- **Branches**:
  - `tests`: Reserved for test-related changes.
  - `models`: Dedicated to model development and backend integration.
- Changes are reviewed and merged into `main` after testing.

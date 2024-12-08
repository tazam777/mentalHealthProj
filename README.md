# **Mental Health Prediction App**

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Architecture](#architecture)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Project Structure](#project-structure)
8. [Endpoints](#endpoints)
9. [Testing](#testing)
10. [Future Enhancements](#future-enhancements)
11. [Contributing](#contributing)

---

## **1. Project Overview**
The **Mental Health Prediction App** is designed to help employees and organizations evaluate whether their environment is mental health-friendly. By leveraging predictive models, this application provides insights based on user input.

The app supports two main prediction models:
- **Employee Model**: Focuses on individual employees and their work environment.
- **Company Model**: Evaluates companies' policies and practices regarding mental health.

This project aims to promote mental health awareness and provide actionable insights.

---

## **2. Features**
- **Interactive Forms**: Collect data from users through intuitive forms for employees and companies.
- **Dynamic Feedback**: Provides predictions and confidence scores.
- **Error Handling**: Displays meaningful error messages for missing or invalid input.
- **Robust API**: Backend endpoints to handle prediction requests.

---

## **3. Tech Stack**
### **Frontend:**
- React.js
- React Router for navigation
- CSS for styling

### **Backend:**
- Flask (Python)
- Joblib for model handling

### **Machine Learning:**
- Scikit-learn for training models and preprocessing

### **Testing:**
- Jest and React Testing Library for frontend tests
- Pytest for backend tests

---

## **4. Architecture**
The application follows a client-server architecture:
1. **Frontend**: A React application that serves as the user interface.
2. **Backend**: A Flask-based API that processes user input and interacts with pre-trained machine learning models.
3. **Machine Learning Models**: Scikit-learn models for predicting mental health-friendliness.

---

## **5. Setup and Installation**
### **Prerequisites:**
- Node.js and npm for the frontend.
- Python 3.x and pip for the backend.

### **Steps:**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mentalHealthProj
   ```

2. **Frontend Setup:**
   - Navigate to the frontend folder:
     ```bash
     cd frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the development server:
     ```bash
     npm start
     ```

3. **Backend Setup:**
   - Navigate to the backend folder:
     ```bash
     cd backend
     ```
   - Set up a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate  # For Windows: env\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Flask server:
     ```bash
     flask run
     ```

---

## **6. Usage**
- **Frontend:**
  - Open the app in your browser at `http://localhost:3000`.
  - Select the Employee or Company model.
  - Fill out the form and click "Submit" to receive predictions.
  
- **Backend:**
  - Use tools like Postman to test the endpoints directly.

---

## **7. Project Structure**
```
mentalHealthProj/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── setupTests.js
│   ├── package.json
│   └── README.md
│
├── backend/
│   ├── scripts/
│   │   ├── companyBack.py
│   │   ├── employeeBack.py
│   │   └── utils/
│   ├── models/
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
└── README.md
```

---

## **8. Endpoints**
### **Company API:**
- **`GET /`**: Health check endpoint.
- **`POST /predict`**: Predicts if a company is mental health-friendly.

### **Employee API:**
- **`GET /`**: Health check endpoint.
- **`POST /predict`**: Predicts if an employee's environment is mental health-friendly.

---

## **9. Testing**
### **Frontend:**
- Run unit tests with Jest:
  ```bash
  npm test
  ```

### **Backend:**
- Run unit and integration tests with Pytest:
  ```bash
  pytest
  ```

---

## **10. Future Enhancements**
- Add visualizations for prediction results.
- Implement more robust input validation.
- Expand datasets for model training to improve prediction accuracy.
- Provide detailed explanations for the predictions.

---

## **11. Contributing**
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with detailed information about your changes.




## 12. Adapting the Project for a Different Dataset

This project is designed to be flexible and can be adapted to work with other datasets to predict outcomes in various domains. Below is a guide on how to modify and extend the project for different datasets and use cases.

---

### Steps to Adapt the Project

1. **Identify a New Dataset**
   - Choose a dataset that fits your target domain and prediction goals.
   - Ensure the dataset includes categorical and/or numerical features that can be preprocessed for machine learning.

2. **Prepare the Dataset**
   - Clean the data: Handle missing values, remove duplicates, and standardize the data.
   - Encode categorical variables: Use `LabelEncoder` or `OneHotEncoder` as required.
   - Split the data into training and testing sets.

3. **Train a New Model**
   - Select a machine learning model suitable for the problem (e.g., Random Forest, Logistic Regression, or Neural Networks).
   - Use a library like scikit-learn to train the model on the new dataset.
   - Save the trained model and any preprocessing artifacts (e.g., scalers, encoders) as `.pkl` files using `joblib`.

4. **Modify the Backend**
   - Replace the model and preprocessing artifact paths in the Flask app (e.g., `companyBack.py` or `employeeBack.py`) with paths to the new `.pkl` files.
   - Update the feature list in the backend script to match the new dataset's features.
   - If feature engineering is required, modify the `preprocess_input` function to include new engineered features.

5. **Update the Frontend**
   - Modify the forms in `EmployeePage.js` or `CompanyPage.js` (or create new pages) to accept input fields corresponding to the new dataset's features.
   - Update the labels and placeholders to provide meaningful guidance for users.

6. **Test the Application**
   - Test both the frontend and backend thoroughly to ensure they work seamlessly with the new dataset.
   - Ensure that predictions and confidence scores are accurate and meaningful.

---

### Examples of Potential Datasets and Use Cases

Here are some examples of datasets and use cases where this project can be adapted:

1. **Healthcare:**
   - Dataset: Patient health records.
   - Purpose: Predict the likelihood of a certain disease or health condition based on patient demographics and symptoms.

2. **Education:**
   - Dataset: Student academic performance.
   - Purpose: Predict student success rates, such as graduation likelihood or test performance, based on historical academic and demographic data.

3. **Customer Retention:**
   - Dataset: Customer behavior and transaction history.
   - Purpose: Predict the likelihood of customer churn for a subscription-based service.

4. **Real Estate:**
   - Dataset: Property listings and historical sales data.
   - Purpose: Predict property prices or the likelihood of a property sale within a given timeframe.

5. **Employee Productivity:**
   - Dataset: Workplace survey data.
   - Purpose: Predict employee satisfaction or productivity based on workplace policies and conditions.

---

### Tips for Success

- **Feature Selection:** Carefully select features from your dataset that are most relevant to the prediction task.
- **Model Choice:** Use exploratory data analysis (EDA) to choose a model that works best for your data.
- **Documentation:** Keep thorough documentation of all changes, including updates to models, features, and user interfaces.
- **Testing:** Ensure that the new application is thoroughly tested to handle edge cases and unseen input values.

---

By following these steps, you can adapt this project to solve a wide range of prediction problems in various fields. The modular structure of the project makes it easy to incorporate new datasets and requirements with minimal effort.
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';

/**
 * LandingPage Component
 * 
 * This component serves as the entry point for the application. It allows users to select
 * between the Employee Model and Company Model to predict mental health outcomes.
 * 
 * Functionalities:
 * - Provides navigation to EmployeePage or CompanyPage using React Router.
 * - Displays a brief introduction to the application.
 */
const LandingPage = () => {
  const navigate = useNavigate(); // Hook for navigation between routes

  return (
    <div className="landing-container">
      {/* Header Section */}
      <div className="landing-header">
        <h1>Welcome to the Mental Health Prediction App</h1>
        <p>Select a model to predict mental health outcomes for employees or companies.</p>
      </div>
      
      {/* Buttons for Navigation */}
      <div className="landing-buttons">
        {/* Navigate to EmployeePage */}
        <button className="landing-button" onClick={() => navigate('/employee')}>
          Employee Model
        </button>
        {/* Navigate to CompanyPage */}
        <button className="landing-button" onClick={() => navigate('/company')}>
          Company Model
        </button>
      </div>
    </div>
  );
};

export default LandingPage;

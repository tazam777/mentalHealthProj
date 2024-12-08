import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div className="landing-container">
      <div className="landing-header">
        <h1>Welcome to the Mental Health Prediction App</h1>
        <p>Select a model to predict mental health outcomes for employees or companies.</p>
      </div>
      <div className="landing-buttons">
        <button className="landing-button" onClick={() => navigate('/employee')}>
          Employee Model
        </button>
        <button className="landing-button" onClick={() => navigate('/company')}>
          Company Model
        </button>
      </div>
    </div>
  );
};

export default LandingPage;

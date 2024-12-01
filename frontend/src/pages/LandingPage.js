import React from 'react';
import { useNavigate } from 'react-router-dom';

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <h1>Welcome to the Mental Health Prediction App</h1>
      <button onClick={() => navigate('/employee')}>Employee Model</button>
      <button onClick={() => navigate('/company')}>Company Model</button>
    </div>
  );
};

export default LandingPage;

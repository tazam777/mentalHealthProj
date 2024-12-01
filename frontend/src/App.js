import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import EmployeePage from './pages/EmployeePage';
import CompanyPage from './pages/CompanyPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/employee" element={<EmployeePage />} />
        <Route path="/company" element={<CompanyPage />} />
      </Routes>
    </Router>
  );
};

export default App;

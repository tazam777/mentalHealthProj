import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import EmployeePage from './pages/EmployeePage';
import CompanyPage from './pages/CompanyPage';

/**
 * App Component
 * This is the root component of the React application. It sets up routing using React Router.
 * The application has three routes:
 * 1. `/` - The landing page.
 * 2. `/employee` - The employee mental health prediction page.
 * 3. `/company` - The company mental health prediction page.
 * 
 * @returns {JSX.Element} The main app component with routing.
 */
const App = () => {
  return (
    // BrowserRouter: Provides routing capabilities for the application.
    <Router>
      {/* Routes: Defines the available routes for the application. */}
      <Routes>
        {/* Route for the landing page */}
        <Route path="/" element={<LandingPage />} />
        
        {/* Route for the EmployeePage component */}
        <Route path="/employee" element={<EmployeePage />} />
        
        {/* Route for the CompanyPage component */}
        <Route path="/company" element={<CompanyPage />} />
      </Routes>
    </Router>
  );
};

// Export the App component as the default export
export default App;

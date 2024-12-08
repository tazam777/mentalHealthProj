import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Import the global CSS styles
import App from './App'; // Import the main App component
import reportWebVitals from './reportWebVitals'; // Import the reportWebVitals function for performance monitoring

/**
 * Entry Point for the React Application
 * 
 * This file is responsible for rendering the root React component (App) into the DOM.
 * It also includes performance monitoring capabilities via `reportWebVitals`.
 */

// Create the root React element using ReactDOM
const root = ReactDOM.createRoot(document.getElementById('root')); // Get the root DOM element

// Render the application
root.render(
  <React.StrictMode>
    {/* StrictMode is a tool for highlighting potential problems in an application */}
    <App /> {/* Main App component */}
  </React.StrictMode>
);

// Call reportWebVitals to measure app performance (optional)
reportWebVitals(); // By default, logs results in the console or sends to an analytics endpoint

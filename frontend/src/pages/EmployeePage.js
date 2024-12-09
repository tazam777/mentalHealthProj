import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { EMPLOYEE_API_URL, fetchPrediction } from "../api/api";
import "./EmployeePage.css";

/**
 * EmployeePage Component
 * 
 * This component provides a form for employees to input their personal details 
 * and workplace environment characteristics to predict if the environment is mental health-friendly.
 * 
 * Functionalities:
 * - Collects user input for various fields related to workplace mental health factors.
 * - Submits data to the prediction API and displays the result.
 * - Includes error handling and a navigation button to return to the home page.
 */
const EmployeePage = () => {
    const navigate = useNavigate(); // Navigation hook for routing
    const [formData, setFormData] = useState({
        self_employed: "",
        work_interfere: "",
        remote_work: "",
        family_history: "",
        benefits: "",
        leave: "",
        care_options: "",
        treatment: "",
    });

    const [result, setResult] = useState(null); // Stores the prediction result
    const [error, setError] = useState(null); // Stores error messages

    /**
     * Updates form data state when input changes.
     * @param {Object} e - The event triggered by input changes.
     */
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    /**
     * Handles form submission, sends data to the prediction API, 
     * and updates result or error state accordingly.
     * @param {Object} e - The form submission event.
     */
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null); // Reset error state
        setResult(null); // Reset result state
        try {
            const response = await fetchPrediction(EMPLOYEE_API_URL, formData); // Fetch prediction from API
            setResult(response); // Store the prediction result
        } catch (err) {
            setError("Error fetching prediction. Please try again."); // Set error message
        }
    };

    return (
        <div className="employee-container">
            <header className="employee-header">
                <h1>Employee Mental Health Prediction</h1>
                <p>
                    Enter your details to predict if your environment is mental health-friendly.
                </p>
            </header>
            <form onSubmit={handleSubmit} className="employee-form">
                {/* Dynamically generate form fields */}
                {[
    { label: "Self-Employed", name: "self_employed", placeholder: "Yes or No" },
    { label: "Work Interfere", name: "work_interfere", placeholder: "Never, Rarely, Sometimes, Often" },
    { label: "Remote Work", name: "remote_work", placeholder: "Yes or No" },
    { label: "Family History", name: "family_history", placeholder: "Yes or No" },
    { label: "Benefits", name: "benefits", placeholder: "Yes, No, Don't Know" },
    { label: "Leave", name: "leave", placeholder: "Very easy, Somewhat easy, Somewhat difficult, Very difficult, Don't Know" },
    { label: "Care Options", name: "care_options", placeholder: "Yes, No, Not Sure" },
    { label: "Treatment", name: "treatment", placeholder: "Yes or No" },
                ].map((field) => (
                    <div className="form-group" key={field.name}>
                        <label htmlFor={field.name}>{field.label}:</label>
                        <input
                            id={field.name}
                            type="text"
                            name={field.name}
                            value={formData[field.name]}
                            onChange={handleChange}
                            placeholder={field.placeholder}
                        />
                    </div>
                ))}
                <button type="submit" className="submit-button">Submit</button>
            </form>
            {error && <p className="error-message">{error}</p>} {/* Display error message */}
            {result && (
                <div className="result-container">
                    <p className="result-message">
                        Prediction: {result.prediction}
                    </p>
                   
                </div>
            )}
            <button className="back-button" onClick={() => navigate("/")}>
                Back to Home
            </button>
        </div>
    );
};

export default EmployeePage;

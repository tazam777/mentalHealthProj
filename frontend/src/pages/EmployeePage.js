import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { EMPLOYEE_API_URL, fetchPrediction } from "../api/api";
import "./EmployeePage.css";

const EmployeePage = () => {
    const navigate = useNavigate();
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

    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        setResult(null);
        try {
            const response = await fetchPrediction(EMPLOYEE_API_URL, formData);
            setResult(response);
        } catch (err) {
            setError("Error fetching prediction. Please try again.");
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
                {[
                    { label: "Self-Employed", name: "self_employed", placeholder: "Yes or No" },
                    { label: "Work Interfere", name: "work_interfere", placeholder: "Rarely, Often, etc." },
                    { label: "Remote Work", name: "remote_work", placeholder: "Yes or No" },
                    { label: "Family History", name: "family_history", placeholder: "Yes or No" },
                    { label: "Benefits", name: "benefits", placeholder: "Yes or No" },
                    { label: "Leave", name: "leave", placeholder: "Very easy, Somewhat easy, etc." },
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
            {error && <p className="error-message">{error}</p>}
            {result && (
                <div className="result-container">
                    <p className="result-message">
                        Prediction: {result.prediction}
                    </p>
                    <p className="result-confidence">
                        Confidence: {result.confidence}%
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

import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { COMPANY_API_URL, fetchPrediction } from "../api/api";
import "./CompanyPage.css";

const CompanyPage = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        benefits: "",
        wellness_program: "",
        anonymity: "",
        leave: "",
        seek_help: "",
        remote_work: "",
        mental_health_consequence: "",
        supervisor: "",
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
            const response = await fetchPrediction(COMPANY_API_URL, formData);
            setResult(response);
        } catch (err) {
            setError("Error fetching prediction. Please try again.");
        }
    };

    return (
        <div className="company-container">
            <header className="company-header">
                <h1>Company Mental Health Prediction</h1>
                <p>
                    Enter details about your company to predict if it’s mental health-friendly.
                </p>
            </header>
            <form onSubmit={handleSubmit} className="company-form">
                {[
                    { label: "Benefits", name: "benefits", placeholder: "Yes or No" },
                    { label: "Wellness Program", name: "wellness_program", placeholder: "Yes or No" },
                    { label: "Anonymity", name: "anonymity", placeholder: "Yes or No" },
                    { label: "Leave", name: "leave", placeholder: "Very easy, Somewhat easy, etc." },
                    { label: "Seek Help", name: "seek_help", placeholder: "Yes or No" },
                    { label: "Remote Work", name: "remote_work", placeholder: "Yes or No" },
                    { label: "Mental Health Consequence", name: "mental_health_consequence", placeholder: "None, Somewhat, etc." },
                    { label: "Supervisor", name: "supervisor", placeholder: "Yes or No" },
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
                        Prediction: {result.mental_health_friendly ? "Mental Health Friendly" : "Not Mental Health Friendly"}
                    </p>
                    <p className="result-confidence">Confidence: {result.confidence}%</p>
                </div>
            )}
            <button className="back-button" onClick={() => navigate("/")}>
                Back to Home
            </button>
        </div>
    );
};

export default CompanyPage;

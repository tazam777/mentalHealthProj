import React, { useState } from "react";
import { COMPANY_API_URL, fetchPrediction } from "../api/api";

const CompanyPage = () => {
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
            setResult(response); // Save the entire response to display both prediction and confidence
        } catch (err) {
            setError("Error fetching prediction. Please try again.");
        }
    };

    return (
        <div className="page-container">
            <h1>Company Mental Health Prediction</h1>
            <form onSubmit={handleSubmit} className="form">
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
                        <label>{field.label}:</label>
                        <input
                            type="text"
                            name={field.name}
                            value={formData[field.name]}
                            onChange={handleChange}
                            placeholder={field.placeholder}
                        />
                    </div>
                ))}
                <button type="submit">Submit</button>
            </form>
            {error && <p className="error-message">{error}</p>}
            {result && (
                <div>
                    <p className="result-message">
                        Prediction: {result.mental_health_friendly ? "Mental Health Friendly" : "Not Mental Health Friendly"}
                    </p>
                    <p className="result-message">Confidence: {result.confidence}%</p>
                </div>
            )}
        </div>
    );
};

export default CompanyPage;

import React, { useState } from "react";
import { EMPLOYEE_API_URL, fetchPrediction } from "../api/api";
import "./style.css"; // Import CSS for styling

const EmployeePage = () => {
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

    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        setPrediction(null);
        try {
            const result = await fetchPrediction(EMPLOYEE_API_URL, formData);
            setPrediction(result.prediction);
        } catch (err) {
            setError("Error fetching prediction. Please try again.");
        }
    };

    
    return (
        <div className="page-container">
            <h1>Employee Mental Health Prediction</h1>
            <form onSubmit={handleSubmit} className="form">
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
            {prediction && <p className="result-message">Prediction: {prediction}</p>}
        </div>
    );
};


export default EmployeePage;

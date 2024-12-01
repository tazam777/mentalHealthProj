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
        <div>
            <h1>Company Mental Health Prediction</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Benefits:</label>
                    <input
                        type="text"
                        name="benefits"
                        value={formData.benefits}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <div>
                    <label>Wellness Program:</label>
                    <input
                        type="text"
                        name="wellness_program"
                        value={formData.wellness_program}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <div>
                    <label>Anonymity:</label>
                    <input
                        type="text"
                        name="anonymity"
                        value={formData.anonymity}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <div>
                    <label>Leave:</label>
                    <input
                        type="text"
                        name="leave"
                        value={formData.leave}
                        onChange={handleChange}
                        placeholder="Very easy, Somewhat easy, etc."
                    />
                </div>
                <div>
                    <label>Seek Help:</label>
                    <input
                        type="text"
                        name="seek_help"
                        value={formData.seek_help}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <div>
                    <label>Remote Work:</label>
                    <input
                        type="text"
                        name="remote_work"
                        value={formData.remote_work}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <div>
                    <label>Mental Health Consequence:</label>
                    <input
                        type="text"
                        name="mental_health_consequence"
                        value={formData.mental_health_consequence}
                        onChange={handleChange}
                        placeholder="None, Somewhat, etc."
                    />
                </div>
                <div>
                    <label>Supervisor:</label>
                    <input
                        type="text"
                        name="supervisor"
                        value={formData.supervisor}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
            {error && <p style={{ color: "red" }}>{error}</p>}
            {result && (
                <div>
                    <p>Prediction: {result.mental_health_friendly ? "Mental Health Friendly" : "Not Mental Health Friendly"}</p>
                    <p>Confidence: {result.confidence}%</p>
                </div>
            )}
        </div>
    );
};

export default CompanyPage;

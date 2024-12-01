import React, { useState } from "react";
import { EMPLOYEE_API_URL, fetchPrediction } from "../api/api";

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
        <div>
            <h1>Employee Mental Health Prediction</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Self-Employed:</label>
                    <input
                        type="text"
                        name="self_employed"
                        value={formData.self_employed}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <div>
                    <label>Work Interfere:</label>
                    <input
                        type="text"
                        name="work_interfere"
                        value={formData.work_interfere}
                        onChange={handleChange}
                        placeholder="Rarely, Often, etc."
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
                    <label>Family History:</label>
                    <input
                        type="text"
                        name="family_history"
                        value={formData.family_history}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
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
                    <label>Care Options:</label>
                    <input
                        type="text"
                        name="care_options"
                        value={formData.care_options}
                        onChange={handleChange}
                        placeholder="Yes, No, Not Sure"
                    />
                </div>
                <div>
                    <label>Treatment:</label>
                    <input
                        type="text"
                        name="treatment"
                        value={formData.treatment}
                        onChange={handleChange}
                        placeholder="Yes or No"
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
            {error && <p style={{ color: "red" }}>{error}</p>}
            {prediction && <p>Prediction: {prediction}</p>}
        </div>
    );
};

export default EmployeePage;

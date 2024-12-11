// Define API URLs
export const EMPLOYEE_API_URL = "http://127.0.0.1:5003/predict";
export const COMPANY_API_URL = "http://127.0.0.1:5001/predict";

// Generic function to fetch predictions from the backend
export const fetchPrediction = async (url, data) => {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data), // Convert data to JSON
        });

        if (!response.ok) {
            throw new Error(`Failed to fetch prediction. Status: ${response.status}`);
        }

        return await response.json(); // Parse the JSON response
    } catch (error) {
        console.error("API call error:", error);
        throw error; // Rethrow error to be handled in the calling function
    }
};

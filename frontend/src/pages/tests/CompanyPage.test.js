import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import CompanyPage from "../CompanyPage";
import * as api from "../../api/api";

jest.mock("../../api/api"); // Mock the API module

describe("CompanyPage Component", () => {
    test("renders all input fields for company form", () => {
        render(<CompanyPage />);

        // Check for input fields
        expect(screen.getByLabelText(/Benefits:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Wellness Program:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Anonymity:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Leave:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Seek Help:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Remote Work:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Mental Health Consequence:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Supervisor:/i)).toBeInTheDocument();
    });

    test("handles valid form submission", async () => {
        // Mock the API response
        api.fetchPrediction.mockResolvedValue({
            mental_health_friendly: true,
            confidence: 95,
        });

        render(<CompanyPage />);

        // Fill out the form
        fireEvent.change(screen.getByLabelText(/Benefits:/i), {
            target: { value: "Yes" },
        });
        fireEvent.change(screen.getByLabelText(/Wellness Program:/i), {
            target: { value: "No" },
        });
        fireEvent.change(screen.getByLabelText(/Anonymity:/i), {
            target: { value: "Yes" },
        });
        fireEvent.change(screen.getByLabelText(/Leave:/i), {
            target: { value: "Very easy" },
        });

        // Submit the form
        fireEvent.click(screen.getByText(/Submit/i));

        // Assert the prediction result
        expect(await screen.findByText(/Prediction:/i)).toBeInTheDocument();
        expect(await screen.findByText(/Confidence: 95%/i)).toBeInTheDocument();
    });

    test("displays error message on API failure", async () => {
        // Mock the API to throw an error
        api.fetchPrediction.mockRejectedValue(new Error("API error"));

        render(<CompanyPage />);

        // Fill out the form
        fireEvent.change(screen.getByLabelText(/Benefits:/i), {
            target: { value: "Yes" },
        });
        fireEvent.change(screen.getByLabelText(/Wellness Program:/i), {
            target: { value: "No" },
        });

        // Submit the form
        fireEvent.click(screen.getByText(/Submit/i));

        // Assert the error message
        expect(await screen.findByText(/Error fetching prediction. Please try again./i)).toBeInTheDocument();
    });

    test("clears previous results on new submission", async () => {
        // Mock the API response for the first submission
        api.fetchPrediction.mockResolvedValueOnce({
            mental_health_friendly: true,
            confidence: 85,
        });

        render(<CompanyPage />);

        // Fill out the form and submit
        fireEvent.change(screen.getByLabelText(/Benefits:/i), {
            target: { value: "Yes" },
        });
        fireEvent.change(screen.getByLabelText(/Wellness Program:/i), {
            target: { value: "No" },
        });
        fireEvent.click(screen.getByText(/Submit/i));

        // Wait for the first result to appear
        expect(await screen.findByText(/Prediction:/i)).toBeInTheDocument();
        expect(await screen.findByText(/Confidence: 85%/i)).toBeInTheDocument();

        // Mock a second API response for the second submission
        api.fetchPrediction.mockResolvedValueOnce({
            mental_health_friendly: false,
            confidence: 65,
        });

        // Change input values and submit again
        fireEvent.change(screen.getByLabelText(/Benefits:/i), {
            target: { value: "No" },
        });
        fireEvent.click(screen.getByText(/Submit/i));

        // Ensure previous result is cleared and new result is displayed
        await waitFor(() => {
            expect(screen.queryByText(/Confidence: 85%/i)).not.toBeInTheDocument();
            expect(screen.findByText(/Confidence: 65%/i)).toBeInTheDocument();
        });
    });

    test("updates input values correctly", () => {
        render(<CompanyPage />);

        const benefitsInput = screen.getByLabelText(/Benefits:/i);
        fireEvent.change(benefitsInput, { target: { value: "Yes" } });
        expect(benefitsInput.value).toBe("Yes");

        const wellnessProgramInput = screen.getByLabelText(/Wellness Program:/i);
        fireEvent.change(wellnessProgramInput, { target: { value: "No" } });
        expect(wellnessProgramInput.value).toBe("No");
    });
});

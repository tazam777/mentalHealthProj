import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import EmployeePage from "../EmployeePage";
import * as api from "../../api/api";

jest.mock("../../api/api"); // Mock the entire API module

describe("EmployeePage Component", () => {
    test("renders the form with all input fields", () => {
        render(<EmployeePage />);

        // Check for input fields
        expect(screen.getByLabelText(/Self-Employed:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Work Interfere:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Remote Work:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Family History:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Benefits:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Leave:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Care Options:/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/Treatment:/i)).toBeInTheDocument();
    });

    test("handles form submission with valid data", async () => {
        // Mock the API response
        api.fetchPrediction.mockResolvedValue({
            prediction: "Mental Health Friendly",
            confidence: 90,
        });

        render(<EmployeePage />);

        // Fill out the form
        fireEvent.change(screen.getByLabelText(/Self-Employed:/i), {
            target: { value: "Yes" },
        });
        fireEvent.change(screen.getByLabelText(/Work Interfere:/i), {
            target: { value: "Rarely" },
        });
        fireEvent.change(screen.getByLabelText(/Remote Work:/i), {
            target: { value: "No" },
        });

        // Submit the form
        fireEvent.click(screen.getByText(/Submit/i));

        // Assert the prediction result
        expect(await screen.findByText(/Prediction:/i)).toBeInTheDocument();
        expect(await screen.findByText(/Confidence: 90%/i)).toBeInTheDocument();
    });

    test("displays error message on API failure", async () => {
        // Mock the API to throw an error
        api.fetchPrediction.mockRejectedValue(new Error("API error"));

        render(<EmployeePage />);

        // Fill out the form
        fireEvent.change(screen.getByLabelText(/Self-Employed:/i), {
            target: { value: "Yes" },
        });
        fireEvent.change(screen.getByLabelText(/Work Interfere:/i), {
            target: { value: "Rarely" },
        });

        // Submit the form
        fireEvent.click(screen.getByText(/Submit/i));

        // Assert the error message
        expect(await screen.findByText(/Error fetching prediction. Please try again./i)).toBeInTheDocument();
    });

    test("clears previous results on new submission", async () => {
        // Mock the API response for the first submission
        api.fetchPrediction.mockResolvedValueOnce({
            prediction: "Mental Health Friendly",
            confidence: 85,
        });

        render(<EmployeePage />);

        // Fill out the form and submit
        fireEvent.change(screen.getByLabelText(/Self-Employed:/i), {
            target: { value: "Yes" },
        });
        fireEvent.change(screen.getByLabelText(/Work Interfere:/i), {
            target: { value: "Rarely" },
        });
        fireEvent.click(screen.getByText(/Submit/i));

        // Wait for the first result to appear
        expect(await screen.findByText(/Prediction:/i)).toBeInTheDocument();
        expect(await screen.findByText(/Confidence: 85%/i)).toBeInTheDocument();

        // Mock a second API response for the second submission
        api.fetchPrediction.mockResolvedValueOnce({
            prediction: "Not Mental Health Friendly",
            confidence: 70,
        });

        // Change input values and submit again
        fireEvent.change(screen.getByLabelText(/Self-Employed:/i), {
            target: { value: "No" },
        });
        fireEvent.click(screen.getByText(/Submit/i));

        // Ensure previous result is cleared and new result is displayed
        await waitFor(() => {
            expect(screen.queryByText(/Confidence: 85%/i)).not.toBeInTheDocument();
            expect(screen.findByText(/Confidence: 70%/i)).toBeInTheDocument();
        });
    });

    test("updates input values correctly", () => {
        render(<EmployeePage />);

        // Verify that input values update correctly when changed
        const selfEmployedInput = screen.getByLabelText(/Self-Employed:/i);
        fireEvent.change(selfEmployedInput, { target: { value: "Yes" } });
        expect(selfEmployedInput.value).toBe("Yes");

        const workInterfereInput = screen.getByLabelText(/Work Interfere:/i);
        fireEvent.change(workInterfereInput, { target: { value: "Rarely" } });
        expect(workInterfereInput.value).toBe("Rarely");
    });
});

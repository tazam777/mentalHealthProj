/**
 * setupTests.js
 *
 * This file is automatically executed before running any test files. 
 * It is used to configure the testing environment for the project. 
 * By importing the `@testing-library/jest-dom` library, this file 
 * extends Jest's assertions to include custom matchers for testing 
 * DOM nodes.
 *
 * Custom matchers include:
 * - `toBeInTheDocument`: Asserts that an element is in the DOM.
 * - `toHaveTextContent`: Checks if an element contains specific text content.
 * - `toBeVisible`: Asserts that an element is visible to the user.
 * - And more...
 * 
 * This setup file helps enhance the readability and usability of tests 
 * written with React Testing Library.
 */

import "@testing-library/jest-dom"; // Extends Jest with custom DOM matchers for assertions

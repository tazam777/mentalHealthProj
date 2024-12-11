/**
 * reportWebVitals
 * 
 * This function is used to measure the performance of the application by collecting
 * Web Vitals metrics. If a callback function (`onPerfEntry`) is provided and it is a valid
 * function, the function dynamically imports the `web-vitals` library and records the
 * following metrics:
 * 
 * - CLS (Cumulative Layout Shift): Measures visual stability.
 * - FID (First Input Delay): Measures responsiveness to user input.
 * - FCP (First Contentful Paint): Measures the time to render the first visible content.
 * - LCP (Largest Contentful Paint): Measures the time to render the largest visible content.
 * - TTFB (Time to First Byte): Measures the time until the server sends the first byte.
 * 
 * @param {Function} onPerfEntry - A callback function to process the performance entries.
 */

const reportWebVitals = (onPerfEntry) => {
    // Check if the onPerfEntry parameter is a valid function
    if (onPerfEntry && onPerfEntry instanceof Function) {
        // Dynamically import the 'web-vitals' library and retrieve its metrics
        import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
            // Record each Web Vital metric using the provided callback function
            getCLS(onPerfEntry);
            getFID(onPerfEntry);
            getFCP(onPerfEntry);
            getLCP(onPerfEntry);
            getTTFB(onPerfEntry);
        });
    }
};

export default reportWebVitals;

import ReactGA from 'react-ga4';

// Initialize Google Analytics
export const initGA = (measurementId) => {
  ReactGA.initialize(measurementId);
};

// Track page views
export const trackPageView = (path) => {
  ReactGA.send({ hitType: "pageview", page: path });
};
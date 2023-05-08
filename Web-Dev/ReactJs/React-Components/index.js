import React from "react";
import { createRoot } from "react-dom";
import App from "./components/App";

const root = createRoot(document.getElementById("root"));

//https://github.com/airbnb/javascript/tree/master/react#naming

// Using App component
root.render(<App />);

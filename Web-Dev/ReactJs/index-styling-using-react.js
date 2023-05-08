//Create a React app from scratch.
//Show a single h1 that says "Good morning" if between midnight and 12PM.
//or "Good Afternoon" if between 12PM and 6PM.
//or "Good evening" if between 6PM and midnight.
//Apply the "heading" style in the styles.css
//Dynamically change the color of the h1 using inline css styles.
//Morning = red, Afternoon = green, Night = blue.

import React from "react";
import { createRoot } from "react-dom";

const root = createRoot(document.getElementById("root"));

let now = new Date();
//now.setHours()
const currentTime = now.getHours();

let message = "Good morning";
let fontColor = "red";
if (currentTime >= 12 && currentTime < 18) {
  message = "Good Afternoon";
  fontColor = "green";
} else if (currentTime >= 18) {
  message = "Good evening";
  fontColor = "blue";
}

root.render(
  <h1 className="heading" style={{ color: fontColor }}>
    {message}
  </h1>
);

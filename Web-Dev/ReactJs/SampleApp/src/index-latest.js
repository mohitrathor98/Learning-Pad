
import React from "react";
import { createRoot } from "react-dom/client";

// The render() method of the react-dom package is
// considered legacy starting react-dom version 18.

// The method is replaced with the createRoot()
// method that is exported from react-dom/client.
const root = createRoot(document.getElementById("root"));

root.render(
  <div>
    <h1>Fruits</h1>
    <ul>
      <li>Banana</li>
      <li>Apple</li>
      <li>Mango</li>
    </ul>
  </div>
);

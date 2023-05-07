
import React from "react";
import { createRoot } from "react-dom/client";

// The render() method of the react-dom package is
// considered legacy starting react-dom version 18.

// The method is replaced with the createRoot()
// method that is exported from react-dom/client.
const root = createRoot(document.getElementById("root"));
const name = "Mohit";
const luckyNum = 26;

root.render(
  <div>
    {/*To insert CSS instead of class use className */}
    <p className="sample" contentEditable="true" spellCheck="false">This is p</p>
    <h1>Fruits</h1>
    <ul>
      <li>Banana</li>
      <li>Apple</li>
      <li>Mango</li>
    </ul>
    {/* We can use JS code here as well
    JS code can be used as shown here under curly braces */}
    <h1>My Name is {name}!</h1>
    <p>My lucky number can be {luckyNum}</p>
  </div>
);

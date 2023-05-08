
import React from "react";
import { createRoot } from "react-dom";

const root = createRoot(document.getElementById("root"));

//https://github.com/airbnb/javascript/tree/master/react#naming

// Heading component
function Heading() {
  return <h1>My Favourite Foods</h1>;
}

root.render(
  <div>
    <Heading />
    <ul>
      <li>Bacon</li>
      <li>Jamon</li>
      <li>Noodles</li>
    </ul>
  </div>
);
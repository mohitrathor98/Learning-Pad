// require dependencies

// Inside react module, Babel compiler
// which is JS compiler, is present
// Babel compiler handles rendering of code
// and making it compatible with any browser
var React = require("react");
var ReactDOM = require("react-dom");

// another way to import dependencies
import React from "react";
import ReactDOM from "react-dom";

//Render is the technique that can redirect a page
//with the help of function render()
// ReactDOM.render(
//   "What TO Show",
//   "Where to Show",
//   "Callback when this render function is completed"
// );
ReactDOM.render(<h1>Hello World!</h1>, document.getElementById("root"));

ReactDOM.render(
    <div>
      <h1>Hello World!</h1>
      <p>This is my first react app</p>
    </div>,
    document.getElementById("root")
  );

// ReactDOM.render has been depreciated in React18
// See: https://bobbyhadz.com/blog/react-reacdom-render-no-longer-supported-in-react-18

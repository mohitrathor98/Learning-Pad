import React, { useState } from "react";

function App() {

    // useState is a hook which let us dynamically change
    // a part of page without rendering the whole page again.

    // useState takes a init value as an argument
    // returns the value and a function which can be called to
    // change the value anytime

    // Now we can use this count with a tag and value of that tag
    // can be changed dynamically
    const [count, setCount] = useState(0);
    const [counter] = useState("ABC");
  
    function increase() {
      setCount(count + 1);
    }
  
    function decrease() {
      setCount(count - 1);
    }
  
    return (
      <div className="container">
        <h1>{count}</h1>
        <h2>{counter}</h2>
        <button onClick={decrease}>-</button>
        <button onClick={increase}>+</button>
      </div>
    );
}

export default App;

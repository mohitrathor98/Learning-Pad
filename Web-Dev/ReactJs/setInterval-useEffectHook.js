import React, { useState, useEffect } from "react";

function getCurrentTime() {
  return new Date().toLocaleTimeString([], { hour12: false });
}

function App() {
  const [time, increaseTime] = useState(getCurrentTime());

  useEffect(() => {
    const intervalId = setInterval(() => {
      // Update the state or perform any action
      increaseTime(getCurrentTime());
    }, 1000); // in ms;

    // Cleanup function to clear the interval when the component unmounts
    return () => {
      clearInterval(intervalId);
    };
  }, []); // The empty dependency array ensures the effect runs only once

  function changeTime() {
    increaseTime(getCurrentTime());
  }

  return (
    <div className="container">
      <h1>{time}</h1>
      <button onClick={changeTime}>Get Time</button>
    </div>
  );
}

export default App;

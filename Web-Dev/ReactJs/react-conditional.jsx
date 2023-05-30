import React from "react";

var isLoggedIn = false;

function Hello() {
  return <h1>Hello</h1>;
}

function loginForm() {
  return (
    <form className="form">
      <input type="text" placeholder="Username" />
      <input type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  );
}

function App() {
  return <div className="container">{isLoggedIn ? Hello() : loginForm()}</div>;
}

export default App;

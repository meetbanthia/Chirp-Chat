import React, { useState } from "react";
import "./App.css";
import { Login } from "./Login";
import { Register } from "./Register";
import "./dark-theme.css";

function App() {
  const [currentForm, setCurrentForm] = useState('login');

  function handleToggleClick() {
    const body = document.querySelector('body');
    body.classList.toggle('dark-mode');
  }

  return (
    <div className="App">
      {currentForm === 'login' ? <Login onFormSwitch={setCurrentForm} /> : <Register onFormSwitch={setCurrentForm} />}
      <button class="toggle-button" onClick={handleToggleClick}>Change Theme</button>
    </div>
  );
}


export default App;

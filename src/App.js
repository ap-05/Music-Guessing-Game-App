import logo from './logo.svg';
import './App.css';
import React, { useState , useRef, useEffect} from 'react';
import io from 'socket.io-client';

const socket = io(); // Connects to socket connection

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          FINAL_PROJECT_TEAM-8
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

import logo from './logo.svg';
import './App.css';
import React, { useState , useRef, useEffect} from 'react';
import io from 'socket.io-client';
import Login from './components/Login';
import Logout from './components/Logout';
import './login.css';
const socket = io(); // Connects to socket connection

function App() {
  return (
    <div className="App">
      <Login />
      <br />
      <Logout />
      
      
    </div>
  );
}

export default App;

import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './header.js';
import Button from 'antd/lib/button';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <Header title="MRUDULA" isLoggedIn={true}/>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <Button type="primary">Button</Button>
      </div>
    );
  }
}

export default App;

import React, { Component } from 'react';
import Header from './components/Header.js'
import Overview from './pages/Overview.js'
import Process from './pages/Process.js'
import Status from './pages/Status.js'
import Graph from './pages/Graph.js'
import Helmet from 'react-helmet'
import { BrowserRouter, Route, Redirect } from 'react-router-dom';
import './App.css';

class App extends Component {

  constructor(props){
    super(props)

    this.state = {

    }

    this.rightItems = [
      {
        label: "Overview",
        to: "/"
      },
      {
        label: "Process Data",
        to: "/process"
      },
      {
        label: "App Status",
        to: "/status"
      }
    ]

    this.leftItems = ["December 4, 2018", "14:12:01"]
  }

  render() {
    return (
      <BrowserRouter>
          <div>
            <div className="App">
              <Header leftItems={this.leftItems} rightItems={this.rightItems} />
            </div>
              {/* Set page title */}
            <Helmet>
              <title>Aqua</title>
            </Helmet>
            <Route exact path="/" component={Overview} />
            <Route exact path="/process" component={Process} />
            <Route exact path="/status" component={Status} />
            <Route exact path="/graph" component={Graph} />
          </div>
      </BrowserRouter>
    );
  }
}

export default App;

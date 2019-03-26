import 'bootstrap/dist/css/bootstrap.css';
import * as React from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import {Alert} from "reactstrap";

import Dashboard from './Dashboard/Dashboard';
import './App.css';

interface IState{
  alert: boolean,
  color: string,
  content: string,
}

class App extends React.Component<{}, IState> {
  constructor(props: any){
    super(props)

    this.state = {
      alert: false,
      color: 'primary',
      content: '',
    }

    this.onDismiss = this.onDismiss.bind(this);
  }

  public setAlert = (color: string, alert: boolean, content: string) => {
    this.setState({
      "alert": alert,
      "color": color,
      "content": content,
    })
  }

  public render() {
    return (
      <div>
        <Router>
          <div className="App">
            <Route 
              exact path="/" 
              render={() => <Dashboard />}/>
          </div>
        </Router>
        <Alert color={this.state.color} isOpen={this.state.alert} toggle={this.onDismiss}>{this.state.content}</Alert>
      </div>
    );
  }

  private onDismiss() {
    this.setState({ alert: false });
  }
}

export default App;

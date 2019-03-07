import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import './List.css'

class List extends Component {

  constructor(props){
    super(props)

  }

  render(){
    return(
      <div className="List">
        {this.props.items.map(item =>
          <div>
            <Route
              path={item.to}
              children={({ match }) => (
                <div>
                  <Link to={item.to}>
                    <div className="ListItem">
                      {item.label}
                    </div>
                  </Link>
                </div>
              )}
            />
          </div>
        )}
      </div>
    )
  }
}

export default List;

import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import './Header.css'

class Header extends Component {

  constructor(props){
    super(props)

  }

  render(){
    return(
      <div className="Header">
        <div className="HeaderLeftContainer">
          {
            this.props.leftItems.map(item =>
              <div className="HeaderItem, LeftHeaderItem">
                {item}
              </div>
            )
          }
        </div>
        <div className="HeaderRightContainer">
          {
            this.props.rightItems.map(item =>
              <div className="HeaderItem, RightHeaderItem">
                <Route
                  path={item.to}
                  children={({ match }) => (
                    <div className={match ? "active, link" : "link"}>
                      <Link to={item.to}>{item.label}</Link>
                    </div>
                  )}
                />
              </div>
            )
          }
        </div>
      </div>
    )
  }
}

export default Header;

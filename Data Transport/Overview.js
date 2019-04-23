import React, { Component } from 'react'
import List from '../components/List.js'

class Overview extends Component {

  constructor(props){
    super(props)

    this.state = {
      items: [
        {
          to: "/graph",
          label: "item 1"
        },
        {
          to: "/graph",
          label: "item 2"
        },
      ]
    }
  }

  render() {
    return (
      <div>
        <List items={this.state.items}/>
      </div>
    );
  }
}

export default Overview;

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
      ],
      sensors: [
      ]
    }
  }

  componentDidMount(){
    fetch('http://localhost:5000/getSensors')
    .then(response => response.json())
    .then(data => this.setState({sensors: data.sensors}))
  }

  render() {

    var items = []

    for (var i = 0; i < this.state.sensors.length; i++) {
      console.log(i)
      var sensor = this.state.sensors[i]
      items.push({to: "/graph" + "/" + sensor.serial, label: sensor.name})
    }


    return (
      <div>
        <List items={items}/>
      </div>
    );
  }
}

export default Overview;

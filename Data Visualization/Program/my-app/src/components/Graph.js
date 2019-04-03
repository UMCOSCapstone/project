import React, { Component } from 'react';
import Highcharts from 'highcharts';
import socketIOClient from "socket.io-client";
import {
  HighchartsChart, Chart, withHighcharts, XAxis, YAxis, Title, Legend, LineSeries
} from 'react-jsx-highcharts';
import './Graph.css'

class Graph extends Component {

  constructor (props) {
    super(props);
    this.addDataPoint = this.addDataPoint.bind(this);

    const now = Date.now();
    this.state = {
        data: []
    }
}

componentDidMount() {
    const socket = socketIOClient("http://localhost:5000/test");
    socket.on("newnumber", data => this.addDataPoint(data.number));
    socket.on("newnum", data2 => this.addDataPoint(data.number1));
  }


  addDataPoint(data){
    var newData = this.state.data.slice(0)

    newData.push(data)

    if(newData.length > 50){
      newData.shift()
    }

    this.setState({
      data: newData
    })
  }


  render() {
    const {data} = this.state;

    return (
      <div className="graph">


        <HighchartsChart>
          <Chart />

          <Title>Two Series</Title>

          <Legend layout="vertical" align="right" verticalAlign="middle" >
            <Legend.Title>Legend</Legend.Title>
          </Legend>

          <XAxis type="datetime">
            <XAxis.Title>X-axis</XAxis.Title>
          </XAxis>

          <YAxis>
            <YAxis.Title>Y-axis</YAxis.Title>
            <LineSeries name="Channel 1" data={this.state.data}/>
          </YAxis>
        </HighchartsChart>

        <HighchartsChart>
          <Chart />



          <Title>Specific</Title>

          <Legend layout="vertical" align="right" verticalAlign="middle" >
            <Legend.Title>Legend</Legend.Title>
          </Legend>

          <XAxis type="datetime">
            <XAxis.Title>X-axis</XAxis.Title>
          </XAxis>

          <YAxis>
            <YAxis.Title>Y-axis</YAxis.Title>
            <LineSeries name="Channel 2" data={this.state.data2}/>
          </YAxis>
        </HighchartsChart>
      </div>
    );
  }
}

export default withHighcharts(Graph, Highcharts);

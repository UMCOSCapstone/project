import React, { Component } from 'react';
import Highcharts from 'highcharts';
import socketIOClient from "socket.io-client";
import {
  HighchartsChart, Chart, withHighcharts, XAxis, YAxis, Title, Legend, LineSeries
} from 'react-jsx-highcharts';
import './Graph.css'
//import { createRandomData, addDataPoint } from '../utils/data-helpers';

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

    var sensorSerial = this.props.match.params.sensorId

    const socket = socketIOClient("http://localhost:5001/test");
    socket.on("newnumber", data => this.addDataPoint(data));
  }


  addDataPoint(data){

    console.log(data)

    if(data.sensorSerial == this.props.match.params.sensorId){
      var newData = this.state.data.slice(0)

      console.log(new Date(data.dateTime.split(' ').join('T')))
      //console.log(data.dateTime)
      newData.push([new Date(data.dateTime.split(' ').join('T')), data.number])

      // if(newData.length > 50){
      //   newData.shift()
      // }

      this.setState({
        data: newData
      })
    }
  }


  render() {
    // const {data} = this.state;

    // console.log(new Date("2019-04-04T10:55:08.841287" + Z))

    const plotOptions = {
      series: {
        pointStart: new Date("2019-04-04T10:55:08.841287Z")
      }
    }

    return (
      <div className="graph">


        <HighchartsChart plotOptions={plotOptions}>
          <Chart />

          <Title>Sensor Data</Title>

          <Legend layout="vertical" align="right" verticalAlign="middle" >
            <Legend.Title>Legend</Legend.Title>
          </Legend>

          <XAxis type="datetime">
            <XAxis.Title>Time</XAxis.Title>
          </XAxis>

          <YAxis>
            <YAxis.Title>Y-axis</YAxis.Title>
            <LineSeries name="Channel 1" data={this.state.data}/>
          </YAxis>
        </HighchartsChart>
      </div>
    );
  }
}

export default withHighcharts(Graph, Highcharts);

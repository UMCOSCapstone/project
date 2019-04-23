import React, { Component } from 'react';
import Highcharts from 'highcharts';
import socketIOClient from "socket.io-client";
import {
  HighchartsChart, Chart, withHighcharts, XAxis, YAxis, Title, Legend, LineSeries
} from 'react-jsx-highcharts';
import './Graph.css'

var jsonData = require('../jsonData.json')

class Graph extends Component {

  constructor (props) {
    super(props);
    this.addDataPoint = this.addDataPoint.bind(this);
    this.handleChange = this.handleChange.bind(this);

    const now = Date.now();

    this.state = {
        data: [],
        jsonData: [1,2,3,4]
    }
}

componentDidMount() {

  // parse jsonData and set this.state.jsonData to the formated version of the jsonData
  var jsonObj = JSON.parse(this.state.jsonData);

  console.log(jsonData)

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

  handleChange(event){
    this.setState({value: event.target.value});
  }


  render() {

    console.log("calling render()")

    var data = this.state.data

    if(this.state.value === 'processed'){
      var data = this.state.jsonData
    }

    const plotOptions = {
      series: {
        pointStart: new Date("2019-04-04T10:55:08.841287Z")
      }
    }

    return (
      
      <div className="container">

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
              <LineSeries name="Channel 1" data={data}/>
            </YAxis>
          </HighchartsChart>
        </div>


    <div className="side">  
      <div className="SideContainer">

          <div className="upSide">
              <h4>Information</h4>
                  <ul>
                      <li>Device:  <b>Light Absorbtion</b></li>
                      <li>Status:  <b>Connected</b></li>
                      <li>Packets: <b>1021/1220</b></li>
                  </ul>
          </div>

          <div className="downSide">
              <form>
                <label>
                  <h4>Options</h4>
                    <select value={this.state.value} onChange={this.handleChange}>
                      <option value="live">Live</option>
                      <option value="raw">Raw</option>
                      <option value="processed">Processed</option>
                    </select>
                </label>
              </form>

              <form>
                <label>
                  <h4>Channel</h4>
                    <select value={this.state.value} onChange={this.handleChange}>
                      <option value="20">20</option>
                      <option value="40">40</option>
                      <option value="80">80</option>
                    </select>
                </label>
              </form>

              <form>
                <label>
                  <h4>Graph View</h4>
                    <select value={this.state.value} onChange={this.handleChange}>
                      <option value="map">Map</option>
                      <option value="timeseries">Time Series</option>
                    </select>
                </label>
              </form>
          </div> 
        </div>
      </div>


      </div>
    );
  }
}

export default withHighcharts(Graph, Highcharts);

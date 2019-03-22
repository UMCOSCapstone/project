import React, { Component } from 'react'
import Highcharts from 'highcharts';
import {
  HighchartsChart, Chart, withHighcharts, XAxis, YAxis, Title, Subtitle, Legend, LineSeries
} from 'react-jsx-highcharts';
import './Graph.css'


const plotOptions = {
  series: {
    pointStart: 2010
  }
};

var jsonData = require("../pop.json");

//const Graph = () => (

class Graph extends Component {

  constructor(props){
    super(props)
    this.state = {
      forData: []
    }
  }


  componentDidMount() {
    this.getFormatedData()
  }

  getFormatedData(){

    var formatedData = []

    var records = jsonData["data"]

    console.log(records)

    for(var i = 0; i < records.length; i++){
      formatedData.push([new Date(records[i]["date"]), i])
    }


    console.log(formatedData)

    this.setState({
      forData: formatedData
    })


  }
  //console.log("Hello World!")

  render(){
    return(
      <div className="GraphContainer">

        <HighchartsChart className="Graph" plotOptions={plotOptions}>
          <Chart />

          <Legend layout="vertical" align="right" verticalAlign="middle" />

          <XAxis>
            <XAxis.Title>Date</XAxis.Title>
          </XAxis>

          <YAxis>
            <YAxis.Title>Temperature (c)</YAxis.Title>
            <LineSeries name="Channel: 20" data={[
                [Date.UTC(1970, 10, 25), 0],
                [Date.UTC(1970, 11,  6), 0.25],
                [Date.UTC(1970, 11, 20), 1.41],
                [Date.UTC(1970, 11, 25), 1.64],
                [Date.UTC(1971, 0,  4), 1.6],
                [Date.UTC(1971, 0, 17), 2.55],
                [Date.UTC(1971, 0, 24), 2.62],
                [Date.UTC(1971, 1,  4), 2.5],
                [Date.UTC(1971, 1, 14), 2.42],
                [Date.UTC(1971, 2,  6), 2.74],
                [Date.UTC(1971, 2, 14), 2.62],
                [Date.UTC(1971, 2, 24), 2.6],
                [Date.UTC(1971, 3,  1), 2.81],
                [Date.UTC(1971, 3, 11), 2.63],
                [Date.UTC(1971, 3, 27), 2.77],
                [Date.UTC(1971, 4,  4), 2.68],
                [Date.UTC(1971, 4,  9), 2.56],
                [Date.UTC(1971, 4, 14), 2.39],
                [Date.UTC(1971, 4, 19), 2.3],
                [Date.UTC(1971, 5,  4), 2],
                [Date.UTC(1971, 5,  9), 1.85],
                [Date.UTC(1971, 5, 14), 1.49],
                [Date.UTC(1971, 5, 19), 1.27],
                [Date.UTC(1971, 5, 24), 0.99],
                [Date.UTC(1971, 5, 29), 0.67],
                [Date.UTC(1971, 6,  3), 0.18],
                [Date.UTC(1971, 6,  4), 0]
            ]} />,

            <LineSeries name="Channel: 40" data={[
                [Date.UTC(1970, 10, 25), 0],
                [Date.UTC(1970, 11,  6), 0.32],
                [Date.UTC(1970, 11, 20), 1.56],
                [Date.UTC(1970, 11, 25), 1.76],
                [Date.UTC(1971, 0,  4), 2.01],
                [Date.UTC(1971, 0, 17), 2.78],
                [Date.UTC(1971, 0, 24), 2.23],
                [Date.UTC(1971, 1,  4), 2.87],
                [Date.UTC(1971, 1, 14), 2.89],
                [Date.UTC(1971, 2,  6), 2.56],
                [Date.UTC(1971, 2, 14), 2.03],
                [Date.UTC(1971, 2, 24), 1.89],
                [Date.UTC(1971, 3,  1), 1.75],
                [Date.UTC(1971, 3, 11), 1.89],
                [Date.UTC(1971, 3, 27), 2.34],
                [Date.UTC(1971, 4,  4), 2.76],
                [Date.UTC(1971, 4,  9), 2.56],
                [Date.UTC(1971, 4, 14), 2.99],
                [Date.UTC(1971, 4, 19), 3.68],
                [Date.UTC(1971, 5,  4), 3.5],
                [Date.UTC(1971, 5,  9), 2.78],
                [Date.UTC(1971, 5, 14), 2.5],
                [Date.UTC(1971, 5, 19), 1.97],
                [Date.UTC(1971, 5, 24), 0.5],
                [Date.UTC(1971, 5, 29), 0.33],
                [Date.UTC(1971, 6,  3), 0.02],
                [Date.UTC(1971, 6,  4), 0]
            ]} />

            <LineSeries name="Actual" data={
              this.state.forData
            } />

          </YAxis>

        </HighchartsChart>

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
                <select>
                  <option value="live">Live</option>
                  <option value="raw">Raw</option>
                  <option value="processed">Processed</option>
                </select>
              </label>
            </form>

            <form>
              <label>
                <h4>Channel</h4>
                <select>
                  <option value="20">20</option>
                  <option value="40">40</option>
                  <option value="80">80</option>
                </select>
              </label>
            </form>

            <form>
              <label>
                <h4>Graph View</h4>
                <select>
                  <option value="map">Map</option>
                  <option value="timeseries">Time Series</option>
                </select>
              </label>
            </form>
          </div>

        </div>

      </div>
    )}
  }

export default withHighcharts(Graph, Highcharts);

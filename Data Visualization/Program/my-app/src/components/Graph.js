import React, { Component } from 'react';
import Highcharts from 'highcharts';
import {
  HighchartsChart, Chart, withHighcharts, XAxis, YAxis, Title, Legend, LineSeries
} from 'react-jsx-highcharts';
import './Graph.css'
import { createRandomData, addDataPoint } from '../utils/data-helpers';

class Graph extends Component {

  constructor (props) {
    super(props);
    this.updateLiveData = this.updateLiveData.bind(this);
    this.handleStartLiveUpdate = this.handleStartLiveUpdate.bind(this);
    this.handleStopLiveUpdate = this.handleStopLiveUpdate.bind(this);

    const now = Date.now();
    this.state = {
      data1: createRandomData(now),
      data2: createRandomData(now),
      liveUpdate: false
    };
  }

  componentDidMount () {
    this.handleStartLiveUpdate();
  }

  updateLiveData () {
    const { data1, data2 } = this.state;

    this.setState({
      data1: addDataPoint(data1),
      data2: addDataPoint(data2)
    });
  }

  handleStartLiveUpdate (e) {
    e && e.preventDefault();
    this.setState({
      liveUpdate: window.setInterval(this.updateLiveData, 1000)
    });
  }

  handleStopLiveUpdate (e) {
    e.preventDefault();
    window.clearInterval(this.state.liveUpdate);
    this.setState({
      liveUpdate: false
    });
  }

//
  render() {
    const { data1, data2, liveUpdate } = this.state;

    return (
      <div className="graph">

        <HighchartsChart>
          <Chart />

          <Title>Only 1 Series</Title>

          <Legend layout="vertical" align="right" verticalAlign="middle" >
            <Legend.Title>Legend</Legend.Title>
          </Legend>

          <XAxis type="datetime">
            <XAxis.Title>Time</XAxis.Title>
          </XAxis>

          <YAxis>
            <YAxis.Title>Pressure (m)</YAxis.Title>
            <LineSeries name="Channel 20" data={data1} />
          </YAxis>
        </HighchartsChart>

        <HighchartsChart>
          <Chart />

          <Title>2 Series</Title>

          <Legend layout="vertical" align="right" verticalAlign="middle" >
            <Legend.Title>Legend</Legend.Title>
          </Legend>

          <XAxis type="datetime">
            <XAxis.Title>Time</XAxis.Title>
          </XAxis>

          <YAxis>
            <YAxis.Title>Pressure (m)</YAxis.Title>
            <LineSeries name="Channel 20" data={data1} />
            <LineSeries name="Channel 40" data={data2} />
          </YAxis>
        </HighchartsChart>


        <div>
          {!liveUpdate && (
            <button className="btn btn-success" onClick={this.handleStartLiveUpdate}>Live update</button>
          )}
          {liveUpdate && (
            <button className="btn btn-danger" onClick={this.handleStopLiveUpdate}>Stop update</button>
          )}
        </div>

      </div>
    );
  }
}

export default withHighcharts(Graph, Highcharts);

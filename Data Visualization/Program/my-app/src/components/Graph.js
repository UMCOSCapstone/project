import React, { Component } from 'react';
import Highcharts from 'highcharts';
import socketIOClient from "socket.io-client";
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

    this.createRandomSeries = this.createRandomSeries.bind(this);
    this.handleAddSeries = this.handleAddSeries.bind(this);
    this.handleRemoveSeries = this.handleRemoveSeries.bind(this);
    this.renderSeries = this.renderSeries.bind(this);

    const now = Date.now();
    this.state = {
      now,
      series: [{
        name: 'Profit',
        data: createRandomData(now, 1e8)
      }],
      seriesCounter: 1,
      data1: createRandomData(now),
      data2: createRandomData(now),
      liveUpdate: false
    };
  }

  handleRemoveSeries (e) {
    e.preventDefault();
    const { series } = this.state;
    const randomIndex = Math.floor(Math.random() * series.length);
    series.splice(randomIndex, 1);

    this.setState({
      series
    });
  }

   renderSeries ({ name, data }) {
    return (
      <LineSeries name={name} key={name} data={data} />
    );
  }

componentDidMount() {
///   this.handleStartLiveUpdate();
    const socket = socketIOClient("http://localhost:5000/test");
    socket.on("newnumber", data => this.handleStartLiveUpdate(data));
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

  createRandomSeries (index) {
    return {
        name: `Series${index}`,
        data: createRandomData(this.state.now, 1e8)
    };
  }



  handleAddSeries(e){
    e.preventDefault();
    let {series, seriesCounter } = this.state;
    seriesCounter++;
    series.push(
        this.createRandomSeries(seriesCounter)
    );

    this.setState({
    series,
    seriesCounter
    });
  }

  handleRemoveSeries(e){
    e.preventDefault();
    const { series } = this.state;
    const randomIndex = Math.floor(Math.random() * series.length);
    series.splice(randomIndex, 1);

    this.setState({
      series
    });
  }

  render() {
    const { data1, data2, liveUpdate } = this.state;

    return (
      <div className="graph">

        <HighchartsChart>
          <Chart />

          <Title>Two Series</Title>

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

        <HighchartsChart>
          <Chart />

          <Title>Specific</Title>

          <Legend layout="vertical" align="right" verticalAlign="middle" >
            <Legend.Title>Legend</Legend.Title>
          </Legend>

          <XAxis type="datetime">
            <XAxis.Title>Wavelength</XAxis.Title>
          </XAxis>

          <YAxis>
            <YAxis.Title>Pressure (m)</YAxis.Title>
            <LineSeries name="Channel 20" data={data1} />
            {this.state.series.map(this.renderSeries)}
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

        <div>
            {liveUpdate && (
                <button className="btn btn-add" onClick={this.handleAddSeries}>Add line series</button>
            )}

            {liveUpdate && (
                <button className="btn btn-remove" onClick={this.handleRemoveSeries}>Remove line series</button>
            )}
        </div>

      </div>
    );
  }
}

export default withHighcharts(Graph, Highcharts);

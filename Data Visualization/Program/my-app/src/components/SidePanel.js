import React, { Component } from 'react';
import './SidePanel.css'

class SidePanel extends Component {

	constructor (props){
		super(props)

		this.state = {}

	}

	render() {
		return(
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
		);
	}
}

export default SidePanel;

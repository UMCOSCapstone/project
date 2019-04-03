import React, { Component } from 'react';
import Graph from './Graph.js'
import SidePanel from './SidePanel.js'
import './GraphContainer.css'
//import './Clock.js'

class GraphContainer extends Component {

	constructor (props){
		super(props)

		this.state = {}
	}

	render() {
		return(
				<div className="container">

					<div className="graph"> <Graph/> </div>
	            	<div className="side">	<SidePanel/> </div>
            	</div>	
		);
	}
}

export default GraphContainer;

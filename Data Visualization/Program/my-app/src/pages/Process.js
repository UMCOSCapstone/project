import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

const styles = theme => ({
  root: {
    width: "100%",
    marginTop: theme.spacing.unit * 3,
    overflowX: "auto"
  },
  table: {
    minWidth: 700
  }
});

//Variables 

let id = 0;
function createData(name, sync, splitS, splitE, bitTime, bitMethod, sensor, lastQC, lastMerge, lastExport, lastProcess, action) {
  id += 1;
  return {id,name, sync, splitS, splitE, bitTime, bitMethod, sensor, lastQC, lastMerge, lastExport, lastProcess, action};
}

//What is shown each rows. Dumb data. 
//The options are buttons.

const rows = [
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>),
  createData("Sensor Name", 10, 90, 120, 1, "SB", <button onclick>Option</button>, "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", "09/12/18 12:10", <button onclick>Option</button>)

   
];

//Properties
function SimpleTable(props) {
  const { classes } = props;

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow id="tabletop">
            <TableCell>Name</TableCell>
            <TableCell align="right">Sync(s)</TableCell>
            <TableCell align="right">Split Start</TableCell>
            <TableCell align="right">Split End</TableCell>
            <TableCell align="right">Bit Time (Min)</TableCell>
            <TableCell align="right">Bin Method</TableCell>
            <TableCell align="right">Sensor Params</TableCell>
            <TableCell align="right">Last QC</TableCell>
            <TableCell align="right">Last Merge</TableCell>
            <TableCell align="right">Last Export</TableCell>
            <TableCell align="right">Last Processing</TableCell>
            <TableCell align="right">Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.id}>
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.sync}</TableCell>
              <TableCell align="right">{row.splitS}</TableCell>
              <TableCell align="right">{row.splitE}</TableCell>
              <TableCell align="right">{row.bitTime}</TableCell>
              <TableCell align="right">{row.bitMethod}</TableCell>
              <TableCell align="right">{row.sensor}</TableCell>
              <TableCell align="right">{row.lastQC}</TableCell>
              <TableCell align="right">{row.lastMerge}</TableCell>
              <TableCell align="right">{row.lastExport}</TableCell>
              <TableCell align="right">{row.lastProcess}</TableCell>
              <TableCell align="right">{row.action}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}

SimpleTable.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(SimpleTable);

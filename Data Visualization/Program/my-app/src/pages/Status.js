import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const CustomTableCell = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
  row: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.background.default,
    },
  },
});

let id = 0;
function createData(category, info) {
  id += 1;
  return {id, category, info};
}

const rows = [
  createData("Data Received (Past Hour)", "854.12 MB"),
  createData("Previous Sync", "Nov 12, 2018 - 14 - 01 - 05 UTC"),
  createData("Available Space(Primary)", "160.42 GB Remaining"),
  createData("Raw Data(Primary)", "9.43 GB Total"),
  createData("Temp Data(Primary)", "22.34 GB Total"),
  createData("Available Space(Secondary)", "299.34 GB Total"),
  createData("Processed Data(Secondary)", "299.34 GB Total"),
  createData("Backup Directory", "/var/backup/external"),
  createData("Available Space(Backup)", "160.42 GB Total"),
  createData("Raw Data(Backup)", "9.34 GB Total"),
  createData("Processed Data(Backup)", "299.34 GB Total")
];

function CustomizedTable(props) {
  const { classes } = props;

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <CustomTableCell>CATEGORY</CustomTableCell>
            <CustomTableCell align="left">INFO</CustomTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow className={classes.row} key={row.id}>
              <CustomTableCell component="th" scope="row">
                {row.category}
              </CustomTableCell>
              <CustomTableCell align="left">{row.info}</CustomTableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}

CustomizedTable.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(CustomizedTable);

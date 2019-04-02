import * as React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import NotificationsIcon from '@material-ui/icons/Notifications';
import { mainListItems } from './listItems';
import SimpleTable from './SimpleTable';
import { Grid } from '@material-ui/core';
import Box from 'src/components/Box';
import Container from 'typedi';
import { EnergyDataSource } from 'src/data';
import { isEmpty } from 'lodash';
import { GraphData } from 'src/model/energy.models';

var LineChart = require("react-chartjs").Line;

const options = {
  title: {
    display: true,
    text: 'Custom Chart Title'
  },
  responsive: true, 
  maintainAspectRatio: false
}

export interface IDashboardState {
  open: boolean,
  data: GraphData,
  expectedCost: string
}

class Dashboard extends React.Component<{}, IDashboardState> {
  private readonly energyDataSource: EnergyDataSource = Container.get(EnergyDataSource);

  constructor(props: any) {
    super(props);
    this.state = {
      open: false,
      expectedCost: '',
      data: this.energyDataSource.getData()
    };
  }

  async componentDidMount() {
    this.setState({data: this.energyDataSource.getData()}, () => console.log(this.state.data));
  }  

  handleDrawerOpen = () => {
    this.setState({ open: true });
  };

  handleDrawerClose = () => {
    this.setState({ open: false });
  };

  render() {

    return (
      <div>
        <CssBaseline />
          <Drawer
              open={this.state.open}
              onClose={this.handleDrawerClose}
            >
              <div>
                <IconButton onClick={this.handleDrawerClose}>
                  <ChevronLeftIcon />
                </IconButton>
              </div>
              <Divider />
              <List>{mainListItems}</List>
            </Drawer>
        <Grid container alignContent='center' alignItems='center' justify='center' spacing={32}>
          <Grid item xs={12}>
            <AppBar
              position="fixed"
            >
              <Box>
                <Toolbar disableGutters={!this.state.open} >
                  <IconButton
                    color="inherit"
                    aria-label="Open drawer"
                    onClick={this.handleDrawerOpen}
                  >
                    <MenuIcon />
                  </IconButton>
                  <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                  >
                    Dashboard
                  </Typography>
                  <IconButton color="inherit">
                    <Badge badgeContent={0} color="secondary">
                      <NotificationsIcon />
                    </Badge>
                  </IconButton>
                </Toolbar>
              </Box>
            </AppBar>
          </Grid>
          <Grid item xs={12}/>
          <Grid item xs={12}/>
          <Grid item xs={6}>
            <Box>
              <Typography variant="h4" gutterBottom component="h2">
                Consumo
              </Typography>
              <SimpleTable />
            </Box>
          </Grid>
          {!isEmpty(this.state.data) ?
            <Grid item xs={6}>
              <Box>
                <Typography variant="h4" gutterBottom component="h2">
                  Consumo 2019
                </Typography>
                <LineChart 
                  data={this.state.data} 
                  options={options}
                  width={250} 
                  height={250}/>
              </Box>
            </Grid>
            :null
          }
        </Grid>
      </div>
    );
  }
}

export default Dashboard;
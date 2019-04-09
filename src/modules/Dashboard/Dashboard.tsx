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
import { ClipLoader } from 'react-spinners';

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
  anualDataByMonth: GraphData | null,
  monthDataDayByDay: any,
  anualData: any,
  monthData: any,
  expectedCost: string,
  loading: boolean,
}

class Dashboard extends React.Component<{}, IDashboardState> {
  private readonly energyDataSource: EnergyDataSource = Container.get(EnergyDataSource);

  constructor(props: any) {
    super(props);
    this.state = {
      open: false,
      expectedCost: '',
      anualDataByMonth: null,
      anualData: null,
      monthData: null,
      monthDataDayByDay: null,
      loading: true
    };
  }

  async componentDidMount() {
    const anualDataByMonth = await this.energyDataSource.getAnualMonthByMonth();
    const monthDataDayByDay = await this.energyDataSource.getMonthlyWasteDayByDay();
    const monthData = await this.energyDataSource.getMonthlyConsume();
    const anualData = await this.energyDataSource.getAnualConsume();
    this.setState({anualDataByMonth, monthDataDayByDay, monthData, anualData, loading: false});
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
          {this.state.loading ? 
          <div
            style={{
                position: 'absolute', left: '50%', top: '50%',
                transform: 'translate(-50%, -50%)'
            }}
          >
            <ClipLoader
              sizeUnit={"px"}
              size={150}
              color={'#123abc'}
              loading={this.state.loading}
            />
            </div>
          :
          <>
            <Grid item xs={6}>
              <Box>
                <Typography variant="h4" gutterBottom component="h2">
                  Consumo 2019 
                </Typography>
                <SimpleTable data={this.state.anualData}/>
              </Box>
            </Grid>
            <Grid item xs={6}>
              <Box>
                <Typography variant="h4" gutterBottom component="h2">
                  Consumo Mensal
                </Typography>
                <SimpleTable data={this.state.monthData}/>
              </Box>
            </Grid>
            {!isEmpty(this.state.anualDataByMonth) ?
              <Grid item xs={6}>
                <Box>
                  <Typography variant="h4" gutterBottom component="h2">
                    Gasto 2019 Detalhado
                  </Typography>
                  <LineChart 
                    data={this.state.anualDataByMonth} 
                    options={options}
                    width={250} 
                    height={250}/>
                </Box>
              </Grid>
              :null
            }
            {!isEmpty(this.state.monthDataDayByDay) ?
              <Grid item xs={6}>
                <Box>
                  <Typography variant="h4" gutterBottom component="h2">
                    Gasto Abril Detalhado
                  </Typography>
                  <LineChart 
                    data={this.state.monthDataDayByDay} 
                    options={options}
                    width={250} 
                    height={250}/>
                </Box>
              </Grid>
              :null
            }
          </>
          }
        </Grid>
      </div>
    );
  }
}

export default Dashboard;
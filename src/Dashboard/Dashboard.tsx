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
import { mainListItems, secondaryListItems } from './listItems';
import SimpleTable from './SimpleTable';
import { Grid } from '@material-ui/core';
import Box from 'src/Components/Box';


class Dashboard extends React.Component {
  state = {
    open: false,
  };

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
              <Divider />
              <List>{secondaryListItems}</List>
            </Drawer>
        <Grid container alignContent='center' alignItems='center' justify='center' spacing={32}>
          <Grid item xs={12}>
            <AppBar
              position="absolute"
            >
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
            </AppBar>
          </Grid>
          <Grid item xs={12}/>
          <Grid item xs={12}>
            <Box>
              <Typography variant="h4" gutterBottom component="h2">
                Consumption
              </Typography>
              <SimpleTable />
            </Box>
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default Dashboard;
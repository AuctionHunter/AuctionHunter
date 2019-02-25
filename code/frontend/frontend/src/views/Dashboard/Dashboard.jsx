import React from "react";
import {Grid} from "@material-ui/core";

// nodejs library to set properties for components
import PropTypes from "prop-types";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// @material-ui/icons

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";
import AuctionCard from "components/Card/Card-Auction";

class Dashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      vehicles: [],
    };
  }

  componentDidMount() {
    fetch("/api/vehicles/")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            vehicles: result.slice(-20),
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      );
  }

  render() {
    const { error, isLoaded, vehicles } = this.state;
    if (error) {
      return <div>API Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
          <Grid container spacing={24}>
            {vehicles.map((car) => {
              return (
                <Grid item xs={6} key={car._id}>
                  <AuctionCard
                      id={car._id}
                      carImage={car.car_image}
                      carName={car.car_name}
                      miles={car.miles}
                      vin={car.vin.slice(5)}
                      damage={car.primary_damage}
                  />
                </Grid>
              )
            })}
          </Grid>
        </div>
      );
    }
  }
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(dashboardStyle)(Dashboard);

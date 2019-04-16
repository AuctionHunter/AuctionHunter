import React from "react";
import { Redirect } from "react-router-dom";
// nodejs library to set properties for components
import PropTypes from "prop-types";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import CustomInput from "components/CustomInput/CustomInput.jsx";
import Button from "components/CustomButtons/Button.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
// @material-ui/icons

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";
import InputLabel from "@material-ui/core/InputLabel";

class Details extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            redirect: false,
            error: null,
            isLoaded: false,
            vehicle: {},
        };
    }

    loadVehicleData(vehicle_id) {
        fetch("/api/vehicles/" + vehicle_id + "/")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        vehicle: result,
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

    componentDidMount() {
        const { vehicle_id } = this.props.match.params;

        if (vehicle_id != null) this.loadVehicleData(vehicle_id);
    }

    render() {
        const { classes } = this.props;
        const { error, isLoaded, vehicle } = this.state;

        if (this.props.match.params.vehicle_id == null) {
           return <Redirect to='/admin/home' />;
        }

        if (error) {
            return <div>API Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
            <div>
                <GridContainer>
                    <GridItem xs={12} sm={12} md={8}>
                        <Card>
                            <CardHeader color="primary">
                                <h4 className={classes.cardTitleWhite}>{vehicle.car_name}</h4>
                                <p className={classes.cardCategoryWhite}>Complete your profile</p>
                            </CardHeader>
                            <CardBody>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={5}>
                                        <CustomInput
                                            labelText="Company (disabled)"
                                            id="company-disabled"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                disabled: true
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={3}>
                                        <CustomInput
                                            labelText="Username"
                                            id="username"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="Email address"
                                            id="email-address"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={6}>
                                        <CustomInput
                                            labelText="First Name"
                                            id="first-name"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={6}>
                                        <CustomInput
                                            labelText="Last Name"
                                            id="last-name"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="City"
                                            id="city"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="Country"
                                            id="country"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="Postal Code"
                                            id="postal-code"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={12}>
                                        <InputLabel style={{color: "#AAAAAA"}}>About me</InputLabel>
                                        <CustomInput
                                            labelText="Lamborghini Mercy, Your chick she so thirsty, I'm in that two seat Lambo."
                                            id="about-me"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                multiline: true,
                                                rows: 5
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                            </CardBody>
                            <CardFooter>
                                <Button color="primary">Update Profile</Button>
                            </CardFooter>
                        </Card>
                    </GridItem>
                </GridContainer>
            </div>
            )
        }
    }
}

Details.propTypes = {
    classes: PropTypes.object.isRequired
};

export default withStyles(dashboardStyle)(Details);

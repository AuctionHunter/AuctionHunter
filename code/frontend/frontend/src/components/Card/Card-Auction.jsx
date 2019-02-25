import React from 'react';
import { Link } from "react-router-dom";
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';

const styles = theme => ({
    card: {
        display: 'flex',
    },
    details: {
        display: 'flex',
        flexDirection: 'column',
    },
    content: {
        flex: '1 0 auto',
    },
    carImg: {
        width: 200,
    }
});

function AuctionCard(props) {
    const {
        classes,
        id,
        carImage,
        carName,
        miles,
        vin,
        damage
    } = props;


    return (
        <Link to={"/admin/details/" + id}>
            <Card className={classes.card}>
                <CardMedia
                    className={classes.carImg}
                    image={carImage}
                    title={carName}
                />
                <div className={classes.details}>
                    <CardContent className={classes.content}>
                        <Typography component="h5" variant="h5">
                            {carName}
                        </Typography>
                        <Typography variant="subtitle2" color="textSecondary">
                            Miles: {miles}
                        </Typography>
                        <Typography variant="subtitle2" color="textSecondary">
                            Damage: {damage}
                        </Typography>
                        <Typography variant="subtitle2" color="textSecondary">
                            Vin: {vin}
                        </Typography>
                    </CardContent>
                </div>
            </Card>
        </Link>
    );
}

AuctionCard.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(AuctionCard);
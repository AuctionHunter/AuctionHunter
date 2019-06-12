var mongoose = require('mongoose')

var auctionhunter = new mongoose.Schema({
  estimated_price: {
    type: String
  },
  car_name: {
    type: String
  },
  miles: {
    type: String
  },
  vin: {
    type: String
  },
  body: {
    type: String
  },
  primary_damage: {
    type: String
  },
  secondary_damage: {
    type: String
  },
  start_code: {
    type: String
  },
  key_fob: {
    type: String
  },
  airbags: {
    type: String
  },
  car_image: {
    type: String
  },
  url: {
    type: String
  },
  value_est: {
    type: Number
  }
},
  {
    collection: 'scrapy_items'
  }
)

module.exports = mongoose.model('AuctionHunter', auctionhunter)

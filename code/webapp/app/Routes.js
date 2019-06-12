'use strict'

var express = require('express')
var auctionRoutes = express.Router()
var auction = require('./Auction')

auctionRoutes.route('/all').get(function (req, res, next) {
  auction.find(function (err, results) {
    if (err) {
      return next(new Error(err))
    }
    res.json(results) // return all todos
  })
})

module.exports = auctionRoutes

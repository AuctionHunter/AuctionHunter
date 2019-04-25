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

auctionRoutes.route('/add').post(function (req, res) {
  auction.create(
    {
      test: req.body.name
    },
    function (error, result) {
      if (error) {
        res.status(400).send('Unable to create new item')
      }
      res.status(200).json(result)
    }
  )
})

module.exports = auctionRoutes

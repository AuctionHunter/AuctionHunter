'use strict'
var express = require('express')
var morgan = require('morgan')
var path = require('path')
var app = express()
var mongoose = require('mongoose')
var bodyParser = require('body-parser')

// Require configuration file defined in app/Config.js
var config = require('./app/Config')

// Connect to database
mongoose.connect(config.DB)

// Sends static files  from the public path directory
app.use(express.static(path.join(__dirname, '/public')))

// Use morgan to log request in dev mode
app.use(morgan('dev'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}))
var port = config.APP_PORT
app.listen(port) // Listen on port defined in config file
console.log('App listening on port ' + port)

var auctionRoutes = require('./app/Routes')
//  Use routes defined in Route.js and prefix it with api
app.use('/api', auctionRoutes)

app.use(function (req, res, next) {
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:' + port)
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE')
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type')
  next()
})
// Server index.html page when request to the root is made
app.get('/', function (req, res, next) {
  res.sendfile('./public/index.html')
})

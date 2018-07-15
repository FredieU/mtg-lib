// Express - Node.js web framework (routes etc.)
const express = require('express');
// Mongoose - Interact with MongoDB
const mongoose = require('mongoose');
// Bodyparser - Get data from request body
const bodyParser = require('body-parser');

// Initialise express
const app = express();

// Bodyparser set up
app.use(bodyParser.json());
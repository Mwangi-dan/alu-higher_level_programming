#!/usr/bin/node
// Displays the status code of a get request
const requestURL = process.argv[2];

const request = require('request');
request(requestURL, function (response) {
  console.log(response.statusCode);
});

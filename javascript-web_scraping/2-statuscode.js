#!/usr/bin/node
// Displays the status code of a get request
const requestURL = process.argv[2];

const request = require('request');
request.get(requestURL).on('repsonse', (response) => {
  console.log('code: ' + response.statusCode)
});

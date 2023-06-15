#!/usr/bin/node
// Displays the status code of a get request
const requestURL = process.argv[2];

const request = require('request');
request(requestURL, (error, response) => {
  if (error) {
    console.log(error);
    return;
  }
  const statusCode = response.statusCode;
  console.log('code: ' + statusCode);
});

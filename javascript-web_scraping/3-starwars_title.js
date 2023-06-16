#!/usr/bin/node
const request = require('request');
const requestURL = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
request(requestURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const bodyJSON = JSON.parse(body);
  console.log(bodyJSON.title);
});

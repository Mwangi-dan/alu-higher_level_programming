#!/usr/bin/node
const request = require('request');
const episodeNumber = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films/:id';
request(requestURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const bodyJSON = JSON.parse(body);
  const results = bodyJSON.results;
  for (const result of results) {
    if (result.episode_id === +episodeNumber) {
      console.log(result.title);
    }
  }
});

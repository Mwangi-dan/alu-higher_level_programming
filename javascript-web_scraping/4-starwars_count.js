#!/usr/bin/node
const request = require('request');
const requestURL = process.argv[2];
request(requestURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const bodyJSON = JSON.parse(body);
  const results = bodyJSON.results;
  let count = 0;
  // results is an array
  for (const result of results) {
    const characters = result.characters;
    // characters is also an array
    for (const chars of characters) {
      if (chars === requestURL[35] + 'people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});

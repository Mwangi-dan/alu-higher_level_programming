#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const mainObj = JSON.parse(body);
  const completed = {};
  mainObj.forEach((obj) => {
    if (obj.completed && completed[obj.userId] === undefined) {
      completed[obj.userId] = 1;
    } else if (obj.completed) {
      completed[obj.userId] += 1;
    }
  });
  console.log(completed);
});

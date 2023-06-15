#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, function (err) {
  if (err) {
    console.error(err);
  }
});

// Used the function callback to show what it means to use =>

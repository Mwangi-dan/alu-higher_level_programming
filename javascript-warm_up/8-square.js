#!/usr/bin/node
const sizeSquare = process.argv[2];
let output = '';
if (isNaN(sizeSquare)) {
  console.log('Missing size');
} else {
  const intSize = +sizeSquare;
  for (let i = 0; i < intSize; i++) {
    for (let j = 0; j < intSize; j++) {
      output += 'X';
    }
    console.log(output);
    output = '';
  }
}

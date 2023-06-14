#!/usr/bin/node
const firstArgv = process.argv[2];
if (firstArgv.isInteger()) {
  console.log('My number: ' + firstArgv);
} else {
  console.log('Not a number');
}

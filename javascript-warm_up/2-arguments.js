#!/usr/bin/node
const argvList = process.argv;
if (argvList.length === 0) {
  console.log('No argument');
} else if (argvList.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

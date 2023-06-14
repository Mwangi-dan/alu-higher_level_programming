#!/usr/bin/node
const argList = process.argv.slice(2);
console.log(Math.max(argList.map(element => parseInt(element, 10))));

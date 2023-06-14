#!/usr/bin/node
const argList = process.argv.slice(2);
const intList = argList.map(element => +element);
console.log(Math.max(...intList));

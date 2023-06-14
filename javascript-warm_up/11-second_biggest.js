#!/usr/bin/node
if (process.argv.length > 2) {
  const argList = process.argv.slice(2);
  const intList = sort(argList.map(element => +element));
  console.log(intList[-2]);
} else {
  console.log(0);
}

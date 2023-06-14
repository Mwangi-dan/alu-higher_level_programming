#!/usr/bin/node
if (process.argv.length > 2) {
  const argList = process.argv.slice(2);
  const intList = argList.map(element => +element);
  console.log(Math.max(...intList));
} else {
  console.log(0);
}

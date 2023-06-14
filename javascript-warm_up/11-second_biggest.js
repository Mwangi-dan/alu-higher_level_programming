#!/usr/bin/node
if (process.argv.length > 2) {
  const argList = process.argv.slice(2);
  const intList = argList.map(element => +element).sort();
  console.log(intList[-2]);
} else {
  console.log(0);
}

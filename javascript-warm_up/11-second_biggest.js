#!/usr/bin/node
if (process.argv.length > 2) {
  const argList = process.argv.slice(2);
  const intList = argList.map(element => +element).sort((a, b) => a - b);
  console.log(intList[intList.length - 2]);
} else if (process.argv.length === 3) {
  console.log(process.argv[3]);
} else {
  console.log(0);
}

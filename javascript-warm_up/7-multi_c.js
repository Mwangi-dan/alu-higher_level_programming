#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let times = +process.argv[2];
  let i = 0;
  while (i < times) {
    console.log('C is fun');
    i++;
  }
}

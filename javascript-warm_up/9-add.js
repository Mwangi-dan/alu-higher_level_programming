#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const sum = +a + +b;
    return sum;
  }
}
if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  const a = process.argv[2]; const b = process.argv[3];
  console.log(add(a, b));
}

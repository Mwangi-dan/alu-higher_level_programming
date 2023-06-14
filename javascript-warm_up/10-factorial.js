#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (Number.isNaN(process.argv[2]) || process.argv.length === 2) {
  console.log('1');
} else {
  console.log(factorial(process.argv[2]));
}

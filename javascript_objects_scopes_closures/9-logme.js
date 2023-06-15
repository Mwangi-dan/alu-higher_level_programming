#!/usr/bin/node
// Counts the number of times a function has been called
exports.logMe = function (item) {
  if (!this.counter) {
    this.counter = 0;
  }
  console.log(this.counter + ': ' + item);
  this.counter++;
};

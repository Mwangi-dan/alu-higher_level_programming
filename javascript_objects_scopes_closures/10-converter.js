#!/usr/bin/node
// Converts number from one base to another
exports.converter = function (base) {
  return function (value) {
    return value.toString(base);
  };
};

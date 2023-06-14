#!/usr/bin/node
// Class that defines a rectangle
module.exports = class Rectangle(width, height) {
  constructor (w, h) {
    this.w = width;
    this.h = height;
  }

  toString {
    return 'Rectangle { width: ${this.w}, height: ${this.height}'
  }
};

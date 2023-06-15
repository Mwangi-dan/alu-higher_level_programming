#!/usr/bin/node
// Square class that inherits from square class in 5-square
const Square5 = require('./5-square');

module.extends = class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.size; i++) {
        let output = '';
        for (let j = 0; j < this.size; j++) {
          output += c;
        }
        console.log(output);
      }
    } else {
      super.print();
    }
  }
};

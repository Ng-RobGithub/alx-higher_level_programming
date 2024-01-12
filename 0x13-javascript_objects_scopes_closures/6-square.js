#!/usr/bin/node
// Importing Square class from 5-square.js
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  // Constructor for Square class
  constructor(size) {
    // Calling constructor of Square class with size
    super(size);
  }

  // Instance method charPrint to print the square using the specified character (default is X)
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    // Printing the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

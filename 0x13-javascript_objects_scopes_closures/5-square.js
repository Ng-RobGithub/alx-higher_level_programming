#!/usr/bin/node
// Importing Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // Constructor for Square class
  constructor(size) {
    // Calling constructor of Rectangle class with size for both width and height
    super(size, size);
  }
}

module.exports = Square;

#!/usr/bin/node
// logMe.js

let count = 0;

// Function to log the number of arguments already printed and the new argument
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};

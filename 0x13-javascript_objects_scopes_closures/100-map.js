#!/usr/bin/node
// Importing the array from 100-data.js
const list = require('./100-data.js').list;

// Using map to create a new array with values multiplied by their index
const newList = list.map((value, index) => value * index);

// Printing the list
console.log(list);
console.log(newList);

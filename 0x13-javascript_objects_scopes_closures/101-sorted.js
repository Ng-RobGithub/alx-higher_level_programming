#!/usr/bin/node
// Importing the dictionary from 101-data.js
const dict = require('./101-data').dict;

// Creating a new dictionary of user ids by occurrence
const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}

// Printing the new dictionary
console.log(newDict);

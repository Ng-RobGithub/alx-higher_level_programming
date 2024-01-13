#!/usr/bin/node
// Function that executes x times a given function
exports.callMeNgRob = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

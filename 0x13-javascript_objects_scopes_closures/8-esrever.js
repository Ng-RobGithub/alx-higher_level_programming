#!/usr/bin/node
// esrever.js

// Function to reverse a list
exports.esrever = function (list) {
  // Copying the original list to avoid modification of the original array
  const reversedList = [...list];

  // Swapping elements to reverse the list
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};


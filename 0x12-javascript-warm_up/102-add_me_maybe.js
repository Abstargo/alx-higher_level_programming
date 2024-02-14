#!/usr/bin/node
// function that increments and calls a function.
exports.addMeMaybe = function (number, theFunction) {
  return theFunction(number += 1);
};

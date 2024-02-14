#!/usr/bin/node
// function that executes x times a function.
exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};

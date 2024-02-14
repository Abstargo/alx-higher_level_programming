#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const mySol = process.argv;
if (mySol.length <= 3) {
  console.log(0);
} else {
  console.log(mySol.sort((x, y) => y - x).slice(3)[0]);
}

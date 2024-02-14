#!/usr/bin/node
// script that prints the first argument passed to it
const argv = process.argv[2];
if (argv === undefined) {
  console.log('No argument');
} else {
  console.log(argv);
}

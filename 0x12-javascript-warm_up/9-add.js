#!/usr/bin/node

const [, , ...args] = process.argv;
const parsed = [parseInt(args[0]), parseInt(args[1])];
function add (a, b) {
  return a + b;
}

if (!isNaN(parsed[0]) && !isNaN(parsed[1])) {
  console.log(add(parsed[0], parsed[1]));
} else {
  console.log('NaN');
}

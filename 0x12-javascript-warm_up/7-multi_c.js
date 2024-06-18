#!/usr/bin/node

const c = 'C is fun';
const args = process.argv[2];
const parsed = parseInt(args);

if (!isNaN(parsed)) {
  for (let i = 1; i <= parsed; i++) {
    console.log(c);
  }
} else {
  console.log('Missing number of occurrences');
}

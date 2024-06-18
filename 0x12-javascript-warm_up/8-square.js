#!/usr/bin/node

const c = 'X';
const args = process.argv[2];
const parsed = parseInt(args);

if (!isNaN(parsed)) {
  for (let i = 0; i < parsed; i++) {
    let row = '';
    for (let j = 0; j < parsed; j++) {
      row += c;
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}

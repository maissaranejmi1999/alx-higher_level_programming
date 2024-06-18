#!/usr/bin/node

const args = process.argv[2];
const chtoin = parseInt(args);
if (!isNaN(chtoin)) {
  console.log('My number: ', chtoin);
} else {
  console.log('Not a number');
}

#!/usr/bin/node

const dict = require('./101-data').dict;
const newdict = {};

for (const userID in dict) {
  const occurrence = dict[userID];

  if (!newdict[occurrence]) {
    newdict[occurrence] = [];
  }

  newdict[occurrence].push(userID);
}

console.log(newdict);

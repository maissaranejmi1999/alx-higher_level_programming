#!/usr/bin/node
const list = require('./100-data').list;
const map1 = list.map((value, index) => value * index)

console.log(list);
console.log(map1);

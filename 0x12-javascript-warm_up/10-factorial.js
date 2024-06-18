#!/usr/bin/node

const args = process.argv[2];
const parsed = parseInt(args);

function factorial (a) {
  let r = 1;
  if (isNaN(a)) {
    return 1;
  }
  for (let i = a; i > 0; i--) {
    r *= i;
  }
  return r;
}

console.log(factorial(parsed));

#!/usr/bin/node
function esrever (list) {
  let len = list.length - 1;
  const x = len / 2;
  for (let i = 0; i < x; i++) {
    const r = list[i];
    list[i] = list[len];
    list[len] = r;
    len--;
  }
  return list;
}
module.exports = { esrever };

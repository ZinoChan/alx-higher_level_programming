#!/usr/bin/node
const dict = require('./101-data').dict;
const map = {};
for (const [key, value] of Object.entries(dict)) {
  if (map[value]) map[value].push(key);
  else map[value] = [key];
}

console.log(map);

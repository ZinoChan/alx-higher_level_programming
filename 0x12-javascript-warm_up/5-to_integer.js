#!/usr/bin/node
const arg = process.argv[2];
const toNum = Number(arg);

console.log(isNaN(toNum) ? 'Not a number' : 'My Number: ' + toNum);

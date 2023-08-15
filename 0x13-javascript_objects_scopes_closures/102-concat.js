#!/usr/bin/node
const fs = require('fs');

function concatFiles (s1, s2, dest) {
  const data1 = fs.readFileSync(s1, 'utf-8');
  const data2 = fs.readFileSync(s2, 'utf-8');
  const res = data1 + data2;

  fs.write(dest, res, 'utf-8');
}

concatFiles(process.argv[2], process.argv[3], process.argv[4]);

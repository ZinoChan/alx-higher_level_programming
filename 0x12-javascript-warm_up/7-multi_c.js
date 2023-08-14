#!/usr/bin/node
let numOfoccurences = Number(process.argv[2]);

if (isNaN(numOfoccurences)) {
  console.log('Missing number of occurrences');
} else {
  while (numOfoccurences > 0) {
    console.log('C is fun');
    numOfoccurences--;
  }
}

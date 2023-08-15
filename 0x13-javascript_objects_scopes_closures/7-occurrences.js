#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, el) => el === searchElement ? count + 1 : count, 0);
};

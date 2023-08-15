#!/usr/bin/node
exports.esrever = function (list) {
  let l = 0; let r = list.length - 1;
  while (l < r) {
    const tmp = list[r];
    list[r] = list[l];
    list[l] = tmp;
    l++;
    r--;
  }
  return list;
};

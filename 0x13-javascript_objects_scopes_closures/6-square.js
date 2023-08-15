#!/usr/bin/node
const ParentSquare = require('./5-square');
module.exports = class Square extends ParentSquare {
  charPrint (char) {
    if (!char) super.print();
    else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += char;
        }
        console.log(row);
      }
    }
  }
};

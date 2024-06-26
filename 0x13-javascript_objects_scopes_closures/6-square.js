#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let j = 0; j < this.height; j++) {
        let row = '';
        for (let i = 0; i < this.width; i++) {
          row += c;
        }
        console.log(row);
      }
    } else {
      super.print(c);
    }
  }
}
module.exports = Square;

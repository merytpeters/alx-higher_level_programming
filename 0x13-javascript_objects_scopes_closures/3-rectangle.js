#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let printer = '';
        for (let j = 0; j < this.width; j++) {
          printer += 'X';
        }
        console.log(printer);
      }
    }
  }
}
module.exports = Rectangle;

#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || this.height <= 0) {
      return {};
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;

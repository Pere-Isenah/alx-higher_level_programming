#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
}
for (let i = 1; i <= x; i++) {
  console.log('x'.repeat(x));
}

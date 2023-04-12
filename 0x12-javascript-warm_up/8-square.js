#!/usr/bin/node
const firstArg = process.argv[2];
if (isNaN(firstArg)) {
  console.log('Missing size');
}
for (let i = 1; i <= firstArg; i++) {
  console.log('x'.repeat(firstArg));
}

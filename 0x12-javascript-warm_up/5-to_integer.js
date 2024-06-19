#!/usr/bin/node
const { argv } = process;
let StrArg = '';
for (let i = 2; i < argv.length; i++) {
  StrArg += argv[i] + ' ';
}
const num = parseInt(StrArg.trim(), 10);
if (argv.length === 1 || isNaN(num)) {
  console.log('Not a number');
} else if (argv.length >= 2) {
  console.log('My number: ' + num);
}

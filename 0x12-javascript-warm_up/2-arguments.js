#!/usr/bin/node
const { argv } = process;
let message;
if (argv.length === 2) {
  message = 'No argument';
} else if (argv.length === 3) {
  message = 'Argument found';
} else if (argv.length >= 4) {
  message = 'Arguments found';
}
console.log(message);

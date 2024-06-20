#!/usr/bin/node
const { argv } = process;
const message = 'C is fun';
const x = parseInt(argv[2], 10);
if (argv.length === 1 || isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(message);
  }
}

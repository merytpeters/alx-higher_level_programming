#!/usr/bin/node
const { argv } = process;
const size = parseInt(argv[2], 10);
if (argv.length === 1 || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let square = '';
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
}

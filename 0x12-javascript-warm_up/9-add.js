#!/usr/bin/node
const { argv } = process;

function add (a, b) {
  console.log(a + b);
}
if (argv.length !== 4) {
  console.log(NaN);
} else {
  const a = parseInt(argv[2], 10);
  const b = parseInt(argv[3], 10);
  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  } else {
    add(a, b);
  }
}

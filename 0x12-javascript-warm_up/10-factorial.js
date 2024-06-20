#!/usr/bin/node
const { argv } = process;

function factorial (n) {
  console.log(n * factorial(n - 1));
}
if (argv.length !== 3) {
  console.log(NaN);
} else {
  const n = parseInt(process.argv[2], 10);
  if (isNaN(n) || n <= 0) {
    console.log(1);
  } else {
    factorial(n);
  }
}

#!/usr/bin/node
const { argv } = process;

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (argv.length !== 3) {
  console.log(1);
} else {
  const num = parseInt(process.argv[2], 10);
  if (isNaN(num) || num < 0) {
    console.log(1);
  } else {
    console.log(factorial(num));
  }
}

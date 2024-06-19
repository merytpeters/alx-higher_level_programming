#!/usr/bin/node
const { argv } = process;
let StrArg = '';
if (argv.length === 3) {
  console.log(argv[2], 'is undefined');
} else if (argv.length >= 3) {
  for (let i = 3; i < argv.length; i++) {
    StrArg += argv[i] + ' ';
  }
  console.log(argv[2] + ' is ' + StrArg);
} else {
  console.log('undefined is undefined');
}

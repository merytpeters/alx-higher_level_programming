#!/usr/bin/node
const { argv } = process;

if (argv.length <= 3) {
  console.log(0);
} else {
  let largestNum = parseInt(argv[2], 10);
  let secondLargest = parseInt(argv[3], 10);

  if (secondLargest > largestNum) {
    [largestNum, secondLargest] = [secondLargest, largestNum];
  }

  for (let i = 4; i < argv.length; i++) {
    const num = parseInt(argv[i], 10);
    if (num > largestNum) {
      secondLargest = largestNum;
      largestNum = num;
    } else if (num < largestNum && num > secondLargest) {
      secondLargest = num;
    }
  }
  console.log(secondLargest);
}

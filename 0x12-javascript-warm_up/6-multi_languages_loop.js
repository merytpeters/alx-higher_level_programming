#!/usr/bin/node
const multi = 'C is fun\nPython is cool\nJavaScript is amazing';
const lines = multi.split('\n');
for (line of lines) {
  console.log(line);
}

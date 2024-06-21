#!/usr/bin/node
const { dict } = require('./101-data');
const NewDict = {};
for (const userID in dict) {
  const occurrences = dict[userID];
  if (occurrences in NewDict) {
    NewDict[occurrences].push(userID);
  } else {
    NewDict[occurrences] = [userID];
  }
}
console.log(NewDict);

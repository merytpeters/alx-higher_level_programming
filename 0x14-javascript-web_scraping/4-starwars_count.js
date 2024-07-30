#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charID = 18;
    let count = 0;

    body.results.forEach(movie => {
      if (movie.characters.some(character => character.includes(charID.toString()))) {
        count++;
      }
    });
    console.log(count);
  }
});

#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = body.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, { json: true }, (err, res, charBody) => {
        if (err) {
          console.log(err);
        }
        console.log(charBody.name);
      });
    });
  }
});

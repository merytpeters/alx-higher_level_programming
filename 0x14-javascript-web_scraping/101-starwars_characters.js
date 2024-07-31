#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

const fetchCharName = (charUrl) => {
  return new Promise((resolve, reject) => {
    request.get(charUrl, { json: true }, (error, response, charBody) => {
      if (error) {
        return reject(error);
      }
      resolve(charBody.name);
    });
  });
};

request.get(url, { json: true }, async (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const characters = body.characters;
  for (const charUrl of characters) {
    const characterName = await fetchCharName(charUrl);
    console.log(characterName);
  }
});

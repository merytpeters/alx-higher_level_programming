#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(body.title);
  }
});

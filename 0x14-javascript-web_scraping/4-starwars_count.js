#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request(url, function (err, response, body) {
  if (!err) {
    const { results } = JSON.parse(body);

    // Using reduce to count movies with characterId 18
    const count = results.reduce((count, film) => {
      const hasCharacterWithId18 = film.characters.find((character) => character.endsWith(`/api/people/${characterId}/`));
      return hasCharacterWithId18 ? count + 1 : count;
    }, 0);

    console.log(count);
  }
});

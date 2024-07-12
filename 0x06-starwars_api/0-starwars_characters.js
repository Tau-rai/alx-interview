#!/usr/bin/node

const request = require('request');

const getMovieCharacters = (movieId) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, { json: true }, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error(`Failed to retrieve data for movie ID ${movieId}`);
      return;
    }

    const charactersUrls = body.characters;

    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (characterError, characterResponse, characterBody) => {
        if (characterError || characterResponse.statusCode !== 200) {
          console.error(`Failed to retrieve character data from ${characterUrl}`);
        } else {
          console.log(characterBody.name);
        }
      });
    });
  });
};

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

getMovieCharacters(movieId);

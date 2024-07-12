#!/usr/bin/node

const request = require('request');

const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(new Error(`Failed to retrieve character data from ${url}`));
      } else {
        resolve(body.name);
      }
    });
  });
};

const getMovieCharacters = (movieId) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, { json: true }, async (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error(new Error(`Failed to retrieve data for movie ID ${movieId}`));
      return;
    }

    const charactersUrls = body.characters;

    for (const characterUrl of charactersUrls) {
      try {
        const characterName = await getCharacterName(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  });
};

const movieId = process.argv[2];
if (!movieId) {
  console.error(new Error('Usage: ./0-starwars_characters.js <movie_id>'));
  process.exit(1);
}

getMovieCharacters(movieId);

#!/usr/bin/node
const { log } = require('console');
const request = require('request');

const characters = [];

const getAllCharacters = (url) => {
  request(url, (error, response, body) => {
    if (error) {
      log(error);
    } else if (response.statusCode !== 200) {
      console.log('An error occured. Status code: ' + response.statusCode);
    } else {
      characters.push(...JSON.parse(body).results);
      if (JSON.parse(body).next) {
        getAllCharacters(JSON.parse(body).next);
      } else {
        request(
          'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
          (innerError, innerResponse, innerBody) => {
            if (innerError) {
              log(innerError);
            } else if (innerResponse.statusCode !== 200) {
              console.log('An error occured. Status code: ' + response.statusCode);
            } else {
              const movie = (JSON.parse(innerBody));
              const movieCharacters = movie.characters;
              for (const char in movieCharacters) {
                log(characters.find(c => c.url === movieCharacters[char])
                  .name);
              }
            }
          }
        );
      }
    }
  });
};

getAllCharacters('https://swapi-api.alx-tools.com/api/people/');

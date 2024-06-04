#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(
	'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
	(error, response, body) => {
		if (error) {
			log(error);
		} else if (response.statusCode !== 200) {
			console.log('An error occured. Status code: ' + response.statusCode);
		} else {
			const movie = (JSON.parse(body));
			const characters = movie.characters;
			for (const char in characters) {
				request(characters[char], (error, response, body) => {
					if (error) {
						log(error);
					} else {
						log(JSON.parse(body).name);
					}
				});
			}
		}
	}
);

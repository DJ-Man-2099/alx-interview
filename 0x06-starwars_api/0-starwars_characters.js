#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(
	'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
	async (error, response, body) => {
		if (error) {
			log(error);
		} else if (response.statusCode !== 200) {
			console.log('An error occured. Status code: ' + response.statusCode);
		} else {
			const movie = (JSON.parse(body));
			const characters = movie.characters;
			for (const char in characters) {
				try {
					const body = await request(characters[char]);
					log(JSON.parse(body).name);
				} catch (error) {
					log(error);
				}
			}
		}
	}
);

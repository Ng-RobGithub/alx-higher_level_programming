#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error(`Error: ${response.statusCode}`);
		return;
	}

	const movie = JSON.parse(body);
	const charactersUrls = movie.characters;

	const printCharacters = async () => {
		for (const characterUrl of charactersUrls) {
			try {
				const characterRes = await new Promise((resolve, reject) => {
					request(characterUrl, (error, response, body) => {
						if (error) {
							reject(error);
							return;
						}
						if (response.statusCode !== 200) {
							reject(`Error: ${response.statusCode}`);
							return;
						}
						resolve(JSON.parse(body).name);
					});
				});
				console.log(characterRes);
			} catch (err) {
				console.error(err);
			}
		}
	};

	printCharacters();
});

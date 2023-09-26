#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const person = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response && response.statusCode !== 200) {
    console.error('status code:', response.statusCode);
    return;
  }
  const filmsData = JSON.parse(body);
  let wedgeAntillesFilms = 0;
  filmsData.results.forEach(film => {
    if (film.characters.includes(person)) wedgeAntillesFilms++;
  });
  console.log(wedgeAntillesFilms);
});

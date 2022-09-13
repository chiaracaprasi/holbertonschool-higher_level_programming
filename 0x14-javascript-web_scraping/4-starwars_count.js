#!/usr/bin/node

const axios = require('axios');
const APIUrl = process.argv[2];

axios
  .get(APIUrl)
  .then((response) => {
    const films = response.data.results;
    let count = 0;
    films.forEach((film) => {
      const characters = film.characters;
      const isPresent = characters.includes(
        'https://swapi-api.hbtn.io/api/people/18/'
      );
      if (isPresent === true) {
        count++;
      }
    });
    console.log(count);
  })
  .catch((error) => {
    console.log('code: ' + error.response.status);
  });

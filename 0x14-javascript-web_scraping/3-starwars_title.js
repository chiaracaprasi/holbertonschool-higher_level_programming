#!/usr/bin/node

const axios = require('axios');
const movieID = process.argv[2];
const APIUrl = 'https://swapi-api.hbtn.io/api/films/' + movieID;

axios
  .get(APIUrl)
  .then((response) => {
    console.log(response.data.title);
  })
  .catch((error) => {
    console.log('code: ' + error.response.status);
  });

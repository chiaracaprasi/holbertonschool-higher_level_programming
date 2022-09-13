#!/usr/bin/node

const axios = require('axios');
const APIUrl = process.argv[2];


axios.get(APIUrl).then((response) => {
    let films = response.data.results;
    let count = 0;
    films.forEach(film => {
        let characters = film.characters;
        let isPresent = characters.includes("/people/18/");
        if (isPresent === true) {
            count++;
        }
    });
    console.log(count);
}).catch((error) => {
    console.log('code: ' + error.response.status);
});

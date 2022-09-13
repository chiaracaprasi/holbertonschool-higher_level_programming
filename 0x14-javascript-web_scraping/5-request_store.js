#!/usr/bin/node

const fs = require('fs');
const axios = require('axios');
const APIUrl = process.argv[2];
const filePath = process.argv[3];

axios
  .get(APIUrl)
  .then((response) => {
    const content = response.data;
    fs.writeFile(filePath, content, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });

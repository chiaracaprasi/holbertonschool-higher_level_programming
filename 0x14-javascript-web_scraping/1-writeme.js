#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const text = process.argv[3];

fs.readFile(filename, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

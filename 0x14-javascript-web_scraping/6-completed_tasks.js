#!/usr/bin/node

const axios = require('axios');
const APIUrl = process.argv[2];

axios.get(APIUrl).then((response) => {
  const todos = response.data;
  const completedDict = {};
  for (const task of todos) {
    if (task.completed === true) {
      if (completedDict[task.userId] !== undefined) {
        completedDict[task.userId] += 1;
      } else {
        completedDict[task.userId] = 1;
      }
    }
  }
  console.log(completedDict);
});

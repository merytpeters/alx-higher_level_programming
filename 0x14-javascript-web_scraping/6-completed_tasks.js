#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = {};

    body.forEach(todo => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});

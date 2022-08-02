#!/usr/bin/node

exports.esrever = function (list) {
  let result = new Array;
  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]);
  }
  return (result);
};

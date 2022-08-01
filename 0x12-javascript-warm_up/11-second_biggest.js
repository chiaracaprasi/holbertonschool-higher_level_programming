#!/usr/bin/node
function secondHighest (arr) {
  const result = arr.sort(function (a, b) { return b - a; })[3];
  return result;
}

if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  const result = secondHighest(process.argv);
  console.log(result);
}

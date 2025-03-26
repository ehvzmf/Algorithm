const input = require('fs').readFileSync('/dev/stdin', 'utf-8').trim().split('\n').map(line => line.split(' ').map(Number));

let maxVal = -1; 
let position = [0, 0];

input.forEach((row, i) => {
  row.forEach((num, j) => {
    if (num > maxVal) {
      maxVal = num;
      position = [i + 1, j + 1];
    }
  });
});

console.log(maxVal);
console.log(position.join(' '));
// https://www.acmicpc.net/problem/8958

let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let num = Number(input[0]);

for (let i = 1; i <= num; i++) { // [0]은 테스트 케이스의 수 
    let count = 0;
    let sum = 0;

    for (let j = 0; j < input[i].length; j++) {
        if (input[i][j] === 'O') {
            count++;
        } else {
            count = 0;
        }
        sum += count;
    }
    console.log(sum);
}
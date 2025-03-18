const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    [...str].forEach(c => console.log(c))
    // str.split('').map(v => console.log(v))
    // for(let i of str) { console.log(i) }
    // console.log(input.join('\n'));
});

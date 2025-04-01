// https://www.acmicpc.net/problem/2439
// 구현

import { createInterface } from "readline"
const rl = createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []

rl.on("line", (line) => {
    const s = line.trim()
    lines.push(s)
}).on(("close"), () => {
    const N = Number(lines[0])
    const arr = lines[1].split(" ").map(Number)
    let answer = [arr[0]];

  
  
  
})
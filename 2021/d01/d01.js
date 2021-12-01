var fs = require("fs");

var inp_array = fs.readFileSync("01.txt").toString().split("\n").map(x => parseInt(x));

function part1(iarr) {
  count = 0;
  lastval = iarr[0]
  for(i = 1; i < iarr.length; i++) {
    if(iarr[i] > lastval) {
      count++;
    }
    lastval = iarr[i];
  }
  return count
}

function part2(iarr) {
  var narr = [];
  for(i = 0; i < iarr.length - 2; i++) {
    narr.push(iarr[i] + iarr[i+1] + iarr[i+2]);
  }
  return part1(narr);
}

console.log(part1(inp_array));
console.log(part2(inp_array));

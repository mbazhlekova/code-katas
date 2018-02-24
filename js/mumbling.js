/* This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd");    // "A-Bb-Ccc-Dddd"
accum("RqaEzty"); // "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt");    // "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z. */

function accum(str) {
  let arr = str.toLowerCase().split("");
  let newArr = arr.map((x, i) => {
    let multiply = x.repeat(i + 1);
    let capitalize = multiply[0].toUpperCase();
    return capitalize.concat(multiply.slice(1, multiply.length));
  });
  return newArr.join("-");
}

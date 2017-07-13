/* The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance. */

function hammingDistance(x, y) {
  return (x ^ y).toString(2).split('').filter(num => num === '1').length;
}
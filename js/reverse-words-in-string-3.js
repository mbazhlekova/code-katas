/* Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order. */

function reverseWords(str) {
  return str.split(' ').map(x => {
    return x.split('').reverse().join('');
  }).join(' ');
}

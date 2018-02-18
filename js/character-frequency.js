/* Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text. This count excludes numbers, spaces and all punctuation marks. Upper and lower case versions of a character are equivalent and the result should all be in lowercase.

The function should return a list of tuples (in Python) or arrays (in other languages) sorted by the most frequent letters first. The Rust implementation should return an ordered BTreeMap. Letters with the same frequency are ordered alphabetically. For example:

  letterFrequency('aaAabb dddDD hhcc')
will return

  [['d',5], ['a',4], ['b',2], ['c',2], ['h',2]]
Letter frequency analysis is often used to analyse simple substitution cipher texts like those created by the Caesar cipher. */

function letterFrequency(text) {
  const editedTextArr = text.replace(/[^A-Za-z]/g, '').toLowerCase().split('');
  let freq = {};
  for (let i = 0; i < editedTextArr.length; i++) {
    if (freq[editedTextArr[i]]) {
      freq[editedTextArr[i]]++;
    } else {
      freq[editedTextArr[i]] = 1
    }
  }
  return Object.keys(freq).sort((a, b) => {
    if (freq[a] < freq[b]) {
      return 1
    } else if (freq[a] > freq[b]) {
      return -1
    } else {
      if (b > a) {
        return -1;
      } else {
        return 1;
      }
    }
  }).map(x => {
    return [x, freq[x]];
  });
}
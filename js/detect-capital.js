/* Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way. */

function detectCapital(str) {
  if (str.match(/^[A-Z]*$/)) {
    return true;
  }
  if (str.match(/^[a-z]+$/)) {
    return true;
  }
  if (str[0] === str[0].toUpperCase()) {
    for (let i = 1; i < str.length; i++) {
      if (str[i] === str[i].toUpperCase()) {
        return false;
      }
    }
    return true;
  }
}

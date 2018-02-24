/* In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out. */

function filterList(list) {
  return list.filter(x => {
    return typeof x !== 'string';
  })
}

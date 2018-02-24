/* Given an array of integers, every element appears twice except for one. Find that single one. */

function singleNumber(arr) {
  return arr.filter((elem, index, self) => {
    return self.indexOf(elem) === self.lastIndexOf(elem);
  });
}

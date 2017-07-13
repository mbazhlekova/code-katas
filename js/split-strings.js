/* Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters 
then it should replace the missing second character of the final pair with an underscore ('_').*/

function solution(str) {

  var pairsArr = str.match(/.{1,2}/g);
  
  return pairsArr.map(x => {
    return x.length < 2 ? x + '_' : x;
  });

}
/* Write a function which takes in numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 
and also a straight double of the same number in num2. */

function tripledouble(num1, num2) {
  
  const first = [...JSON.stringify(num1).split('')];
  const second = [...JSON.stringify(num2).split('')];

  
    const triple = first
   .filter((v, k) => v === first[k+1] && v === first[k+2]);

  const double = second
   .filter((v, k) => v === second[k+1]);
   
     const result = triple
    .filter(trip => double
    .find(dub => dub === trip)) 

  return result.length >= 1 ? 1 : 0;
}
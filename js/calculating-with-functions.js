/* This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand. */

var calc = function(num, operation) {
  if (!operation) 
    return num;
  return operation(num);
}

function zero(operation) {return calc(0, operation);}
function one(operation) {return calc(1, operation);}
function two(operation) { return calc(2, operation);}
function three(operation) {return calc(3, operation);}
function four(operation) {return calc(4, operation);}
function five(operation) {return calc(5, operation);}
function six(operation) {return calc(6, operation);}
function seven(operation) {return calc(7, operation);}
function eight(operation) {return calc(8, operation);}
function nine(operation) {return calc(9, operation);}

function plus(a) { 
  return function(b) { 
    return b + a; 
    }
  
}
function minus(a) {
  return function(b) { 
    return b - a; 
    
  }
  
}
function times(a) {
  return function(b) {
    return b * a;
  }
}
function dividedBy(a) {
  return function(b) {
    return b / a;
  }
}
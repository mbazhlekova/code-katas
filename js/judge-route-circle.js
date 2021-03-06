/* Initially, there is a Robot at position (0, 0).
Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:

Input: "UD"
Output: true

Example 2:

Input: "LL"
Output: false

Source: Leetcode */

function judgeCircle(moves) {
  const movesArr = moves.split("");
  var pos = {
    x: 0,
    y: 0
  };
  for (let i = 0; i < movesArr.length; i++) {
    switch (movesArr[i]) {
      case "U":
        pos.y = pos.y + 1;
        break;
      case "D":
        pos.y = pos.y - 1;
        break;
      case "L":
        pos.x = pos.x - 1;
        break;
      case "R":
        pos.x = pos.x + 1;
        break;
    }
  }
  if (pos.x === 0 && pos.y === 0) {
    return true;
  }
  return false;
}

// O(n) running time because for loop must iterate over n array items
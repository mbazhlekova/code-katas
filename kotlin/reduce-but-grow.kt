/* 
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24 

*/

package reducebutgrow

fun grow(arr: IntArray): Int {
    return arr.reduce { sum, element -> sum * element }
}


/* Convert number to reversed array of digits

Given a random number:

    C#: long;
    C++: unsigned long;

You have to return the digits of this number within an array in reverse order.
Example:

348597 => [7,9,5,8,4,3]
*/

public class Kata {
  public static int[] digitize(long n) {
    String numString = String.valueOf(n);
    int digits[] = new int[numString.length()];
    int counter = 0;
    
    for (int i = numString.length() - 1; i >= 0; i--) {
      digits[i] = Integer.parseInt(Character.toString(numString.charAt(counter++)));
    }
    
    return digits;
  }
}

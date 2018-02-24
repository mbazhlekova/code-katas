/* I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that */

public static int[] humanYearsCatYearsDogYears(final int humanYears) {
  int catAge;
  int dogAge;
  if (humanYears == 1) {
    catAge = 15;
    dogAge = 15;
  }
  else if (humanYears == 2) {
    catAge = 15 + 9;
    dogAge = 15 + 9;
  }
  else {
    catAge = (15 + 9 + (4 * (humanYears - 2)));
    dogAge = (15 + 9 + (5 * (humanYears - 2)));
  }
  return new int[]{humanYears,catAge,dogAge};
}
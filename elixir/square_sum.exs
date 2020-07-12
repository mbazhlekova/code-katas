@doc """
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""

defmodule SquareSum do
  def square_sum(nums) do
    nums
    |>Enum.map(fn num -> :math.pow(num, 2) end)
    |>Enum.sum
  end
end
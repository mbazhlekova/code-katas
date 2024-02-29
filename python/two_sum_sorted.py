class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while r > l:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
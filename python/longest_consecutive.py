class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

tmp = Solution
print(tmp.longestConsecutive(tmp, [1, 5, 2, 3, 4]))


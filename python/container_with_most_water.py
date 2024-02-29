class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        l, r = 0, len(height) - 1

        while l != r:
            if height[l] <= height[r]:
                max = height[l] * (r - l)
                l += 1
            elif height[l] > height[r]:
                max = height[r] + (r - l)
                r -= 1

        return max
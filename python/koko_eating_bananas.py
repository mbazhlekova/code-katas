from math import ceil


class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = ceil(sum(piles)/h), max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2
            hrs = 0
            for p in piles:
                hrs += ceil(p/k)

            if hrs > h:
                l = k + 1
            else:
                res = k
                r = k - 1

        return res

tmp = Solution
print(tmp.minEatingSpeed(tmp, [3, 6, 7, 11], 8))
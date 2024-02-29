class Solution:
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]

tmp = Solution
print(tmp.carFleet(tmp, 100, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

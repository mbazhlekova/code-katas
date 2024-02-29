class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []  # push [temp, index] onto stack

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t, i))

        return res

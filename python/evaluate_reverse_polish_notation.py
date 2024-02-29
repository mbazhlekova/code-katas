import math


class Solution:
    def evalRPN(self, tokens):
        stack = []
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: y - x,
              '*': lambda x, y: x * y,
              '/': lambda x, y: int(float(y) / x)}

        for t in tokens:
            if not t.lstrip('-').isnumeric():
                stack.append(op[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))

        return stack[0]

tmp = Solution
print(tmp.evalRPN(tmp, ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


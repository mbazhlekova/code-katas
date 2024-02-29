class MinStack:

    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val):
        self.items.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self):
        self.items.pop()
        self.min.pop()

    def top(self):
        return self.items[-1]

    def getMin(self):
        return self.min[-1]

tmp = MinStack()
tmp.push(1)
tmp.push(-2)
tmp.pop()
print(tmp.top())
print(tmp.getMin())
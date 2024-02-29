from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        self.store[key].append((value, timestamp))

    def get(self, key, timestamp):
        values = self.store[key]
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1

        if left == 0:
            return ""
        else:
            return values[left - 1][1]


tmp = TimeMap()
tmp.set("foo", "bar", 1)
print(tmp.get("foo", 1))

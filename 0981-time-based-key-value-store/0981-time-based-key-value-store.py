class TimeMap:
    def __init__(self):
        self.storage = defaultdict(list) # {"foo": [(1, "bar")]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            l = 0
            r = len(self.storage[key]) - 1
            while l <= r:
                m = (l + r) // 2
                if self.storage[key][m][0] == timestamp:
                    return self.storage[key][m][1]
                if self.storage[key][m][0] < timestamp:
                    l = m + 1
                else:
                    r = m - 1
            return "" if r < 0 else self.storage[key][r][1]

        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
class TimeMap:
    def __init__(self):
        self.count = defaultdict(list) # (teimstamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.count[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.count: return ""
        values = self.count[key]
        l = 0
        r = len(values) - 1
        maxItem = (float('-inf'), "")
        while l <= r:
            m = (l + r) // 2
            if timestamp >= values[m][0]:
                maxItem = values[m]
                l = m + 1
            else:
                r = m - 1
        return maxItem[1] if maxItem[0] != float('-inf') else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
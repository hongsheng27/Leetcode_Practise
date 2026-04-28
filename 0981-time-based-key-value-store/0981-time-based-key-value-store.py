class TimeMap:
    def __init__(self):
        self.record = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.record:
            self.record[key] = []
        self.record[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.record: return ""
        l = 0
        r = len(self.record[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.record[key][m][0] > timestamp:
                r = m - 1
            elif self.record[key][m][0] < timestamp:
                l = m + 1
            else:
                return self.record[key][m][1]
        return "" if r < 0 else self.record[key][r][1]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
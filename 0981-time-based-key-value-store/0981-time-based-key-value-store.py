class TimeMap:
    def __init__(self):
        self.count = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.count:
            self.count[key] = [(timestamp, value)]
        else:
            self.count[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.count: return ""
        lst = self.count[key]
        l = 0
        r = len(lst) - 1
        while l <= r:
            m = (l + r) // 2
            if lst[m][0] == timestamp: return lst[m][1]
            if lst[m][0] < timestamp: 
                l = m + 1
            else:
                r = m - 1
        return lst[r][1] if r >= 0 and lst[r] else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
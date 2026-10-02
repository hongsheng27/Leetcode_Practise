class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)
        # {"foo": [(1, "bar"), (4, "bar2")]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        l = 0
        r = len(self.map[key]) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if timestamp >= self.map[key][m][0]:
                res = self.map[key][m][1]
                l = m + 1
            else:
                r = m - 1  
        return res

        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
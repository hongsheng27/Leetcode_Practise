class TimeMap:
    def __init__(self):
        self.storage = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        res = (timestamp, value)
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append(res)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            l, r = 0, len(self.storage[key]) - 1
            
            while l <= r:
                m = (l + r) // 2
                if self.storage[key][m][0] < timestamp:
                    l = m + 1
                elif self.storage[key][m][0] > timestamp:
                    r = m - 1
                else:
                    return self.storage[key][m][1]
            return self.storage[key][r][1] if 0 <= r <= len(self.storage[key]) - 1 else ""
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
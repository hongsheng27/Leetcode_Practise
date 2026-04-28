class TimeMap:
    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            values = self.store.get(key, [])
            l, r = 0, len(values) - 1
            
            while l <= r:
                m = (l + r) // 2
                if self.store[key][m][0] < timestamp:
                    l = m + 1
                elif self.store[key][m][0] > timestamp:
                    r = m - 1
                else:
                    return self.store[key][m][1]
            # if no found, r is the closest index to the answer
            return self.store[key][r][1] if 0 <= r <= len(self.store[key]) - 1 else ""
        else:
            return ""
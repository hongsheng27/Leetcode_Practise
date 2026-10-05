class RecentCounter:
    # solution1: mantain 3000 fixed window, onece the new ping over it, start from 0 index
    # but I need one more variable to save next start index
    # when ping, return sum()
    # solution2: maybe using queue so that I can use popleft and append directly
    def __init__(self):
        self.q = deque([0] * 3001)
        self.requestNumber = 0
        self.preT = 0
        
    def ping(self, t: int) -> int:
        gap = (t - self.preT) 
        if gap >= 3001:
            self.q = deque([0] * 3000 + [1])
            self.preT = t
            self.requestNumber = 1
            return self.requestNumber
        
        for i in range(gap):
            elem = self.q.popleft()
            if elem == 1: 
                self.requestNumber -= 1
            if i + 1 == gap:
                self.q.append(1) # 1 mean request
            else:
                self.q.append(0)
        self.preT = t
        self.requestNumber += 1
        return self.requestNumber


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
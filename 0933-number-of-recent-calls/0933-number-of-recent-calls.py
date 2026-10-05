class RecentCounter:
    # solution1: mantain 3000 fixed window, onece the new ping over it, start from 0 index
    # but I need one more variable to save next start index
    # when ping, return sum()
    # solution2: maybe using queue so that I can use popleft and append directly
    def __init__(self):
        self.q = deque([])
        
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
        
# obj = RecentCounter()
# param_1 = obj.ping(t)
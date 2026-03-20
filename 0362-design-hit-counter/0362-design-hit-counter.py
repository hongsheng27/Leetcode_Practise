class HitCounter:
    def __init__(self):
        self.hits = []
        self.l = 0
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.l < len(self.hits) and timestamp - self.hits[self.l] >= 300:
            self.l += 1
        return len(self.hits) - self.l
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
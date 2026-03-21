class HitCounter:
    def __init__(self):
        self.hits = [0] * 300
        self.counts = [0] * 300
    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        if self.hits[index] != timestamp:
            self.hits[index] = timestamp
            self.counts[index] = 1
        else:
            self.hits[index] = timestamp
            self.counts[index] += 1


    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(len(self.hits)):
            if timestamp - self.hits[i] < 300:
                total += self.counts[i]
        return total
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
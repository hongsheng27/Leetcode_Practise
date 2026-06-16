class MedianFinder:
    def __init__(self):
        self.smalls = [] # maxHeap
        self.bigs = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smalls, -num)
        num = heapq.heappop(self.smalls)
        heapq.heappush(self.bigs, -num)
        if len(self.bigs) > len(self.smalls):
            num = heapq.heappop(self.bigs)
            heapq.heappush(self.smalls, -num)

    def findMedian(self) -> float:
        if len(self.smalls) == len(self.bigs):
            return (-self.smalls[0] + self.bigs[0]) / 2
        return -self.smalls[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
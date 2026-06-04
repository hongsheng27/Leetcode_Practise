class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap: 
            heapq.heappush(self.maxHeap, -num)
        elif self.minHeap and num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        # swap
        if len(self.maxHeap) < len(self.minHeap):
            elem = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -elem)
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            elem = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -elem)
        
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
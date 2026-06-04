class MedianFinder:
    def __init__(self):
        self.maxHeap = [] # smaller half
        self.minHeap = [] # larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        # decide which side
        value = heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, -value)
        # swap
        if len(self.minHeap) > len(self.maxHeap):
            value = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -value)
        
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
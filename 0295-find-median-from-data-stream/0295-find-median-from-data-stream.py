class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        index = (len(self.nums) - 1) // 2
        if len(self.nums) % 2 == 0:
            return (self.nums[index] + self.nums[index + 1]) / 2
        else:
            return self.nums[index]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
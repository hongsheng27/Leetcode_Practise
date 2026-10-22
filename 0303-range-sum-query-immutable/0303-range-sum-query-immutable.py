class NumArray:
    # brute force: travese from start to end => O(N)
    # optimal prefix => O(1), prefix[end] - prefix[start] - 1
    def __init__(self, nums: list[int]):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        left = self.prefix[left - 1] if left > 0 else 0
        return self.prefix[right] - left
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
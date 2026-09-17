class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = res = 0
        for n in nums:
            position += n
            if position == 0:
                res += 1
        return res
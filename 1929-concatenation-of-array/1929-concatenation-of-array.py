class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n * 2):
            i = i % n 
            res.append(nums[i])
        return res
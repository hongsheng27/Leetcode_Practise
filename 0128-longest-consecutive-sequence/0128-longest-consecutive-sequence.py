class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for s in seen:      
            if s - 1 not in seen:  
                longest = 0
                while s in seen:
                    s += 1
                    longest += 1
                res = max(res, longest)
        return res

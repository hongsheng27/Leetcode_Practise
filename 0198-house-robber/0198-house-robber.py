class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def recursion(i):
            if i >= len(nums): 
                return 0
            if i in cache: return cache[i]
            cache[i] = max(nums[i] + recursion(i + 2),
                           recursion(i + 1))
            return cache[i]
            
        return recursion(0)

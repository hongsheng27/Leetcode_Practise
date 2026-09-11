class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursion(i, total, cache):
            if i >= len(nums): 
                return total
            if (i, total) in cache: return cache[(i, total)]
            cache[(i, total)] = max(recursion(i + 2, total + nums[i], cache),
                                    recursion(i + 1, total, cache))
            return cache[(i, total)]
        return recursion(0, 0, {})

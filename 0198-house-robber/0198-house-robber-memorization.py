class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums): return 0
            if i in cache: return cache[i]
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]
        return dfs(0)
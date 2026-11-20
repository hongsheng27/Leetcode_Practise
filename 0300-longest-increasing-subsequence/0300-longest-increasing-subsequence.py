class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = {}
        def dfs(i):
            if i in cache: return cache[i]
            if i >= len(nums): return 0

            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
            cache[i] = best
            
            return cache[i]

        for i in range(len(nums)):
            dfs(i)
        
        return max(cache.values())
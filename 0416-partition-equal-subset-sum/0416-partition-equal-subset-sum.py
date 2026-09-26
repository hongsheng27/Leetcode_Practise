class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        cache = {}
        def dfs(i,remaining):
            if remaining == 0:
                return True
            if (i, remaining) in cache: return cache[(i, remaining)]
            if i >= len(nums) or remaining < 0: return False
            cache[(i, remaining)] = dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)
            return cache[(i, remaining)]
    
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        return dfs(0, target)

        
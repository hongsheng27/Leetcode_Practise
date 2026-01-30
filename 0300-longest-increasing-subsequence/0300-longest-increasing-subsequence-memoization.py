class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {len(nums): 1}
        def dfs(i):
            if i in cache: return cache[i]
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            cache[i] = res
            return res
        return max(dfs(i) for i in range(len(nums)))
        
        
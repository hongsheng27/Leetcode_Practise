class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # brute force: dfs, tc: n of target(heiht), sc: target
        res = 0
        cache = {}
        def dfs(total):
            nonlocal res
            if total == target: 
                return 1
            if total > target: return 0
            if total in cache: return cache[total]

            much = 0
            for i in range(len(nums)):
                much += dfs(total + nums[i])
            cache[total] = much
            
            return cache[total]
        return dfs(0)

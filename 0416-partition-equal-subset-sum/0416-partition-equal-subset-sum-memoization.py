class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for n in nums:
            total += n
        if total % 2 != 0: return False
        target = total // 2
        M = len(nums)
        cache = [[-1] * (target + 1) for _ in range(M)]
        def dfs(i, sum):
            if sum == target:
                return True
            if i >= M or sum > target:
                return False
            if cache[i][sum] != -1: return cache[i][sum]
            cache[i][sum] = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum)   
            return cache[i][sum]
        return dfs(0, 0)
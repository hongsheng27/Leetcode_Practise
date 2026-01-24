class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for n in nums:
            total += n
        if total % 2 != 0: return False
        nums.sort()
        
        M, N = len(nums), total // 2 + 1
        cache = [[-1] * N for _ in range(M)]
        def dfs(i, sum):
            if sum == total / 2:
                return True
            if i >= len(nums) or sum > total / 2:
                return False
            if cache[i][sum] != -1: return cache[i][sum]
            cache[i][sum] = dfs(i + 1, sum + nums[i]) or dfs(i + 1, sum)   
            return cache[i][sum]
        return dfs(0, 0)
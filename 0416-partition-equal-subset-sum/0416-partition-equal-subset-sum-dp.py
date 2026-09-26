class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if total % 2 != 0: return False

        M = len(nums)
        target = total // 2 
        dp = [[False] * (target + 1) for _ in range(M)]

        for i in range(M):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, M):
            for j in range(1, target + 1):
                skip = dp[i - 1][j]
                include = False
                if j >= nums[i]:
                    include = dp[i-1][j - nums[i]]
                dp[i][j] = include or skip
        return dp[M - 1][target]
        
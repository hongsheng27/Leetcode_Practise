class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3: return min(cost[0], cost[1])

        dp = [cost[-2], cost[-1]]
        i = len(cost) - 3
        while i >= 0:
            tmp = dp[0]
            dp[0] = min(cost[i] + dp[0], cost[i] + dp[1])
            dp[1] = tmp
            i -= 1
        return min(dp[0], dp[1])
        
        
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = cost[:2]

        for i in range(2, n):
            cur = min(dp[0], dp[1]) + cost[i]
            dp[0] = dp[1]
            dp[1] = cur
            
        return min(dp[0], dp[1])
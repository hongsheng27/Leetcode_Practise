class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # dp[i] =>  min cost to reach step i, including cost[i]
        # dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        n = len(cost)
        dp = list(cost) 
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])

        


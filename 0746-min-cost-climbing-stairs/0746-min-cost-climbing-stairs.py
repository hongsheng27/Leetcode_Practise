class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # dp[i] => minimum cost to i
        # dp[i] = min(dp[i - 1], dp[i - 2])
        n = len(cost)
        cost += [0]
        dp = list(cost) 
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        print(dp)
        return dp[-1]

        


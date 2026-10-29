class Solution:
    def numSquares(self, n: int) -> int:
        # Goal: minimum number of perfect squares that sum to n
        # State: dp[i] = minimum number of perfect squares needed to form i
        # Choices: use any perfect square p <= i as the last number
        # Transition: dp[i] = min(dp[i], dp[i - p] + 1)
        # Base Case: dp[0] = 0
        #
        # P = floor(sqrt(n)), since p = j*j and j*j <= n
        # Generate perfect squares: O(sqrt(n))
        # DP: O(n * P) = O(n * sqrt(n))
        # Space: O(n) for dp + O(sqrt(n)) for perfects = O(n)
        perfects = []
        start = 1
        while start * start <= n:
            perfects.append(start * start)
            start += 1
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, (n + 1)):
            for perfect in perfects:
                if i >= perfect:
                    dp[i] = min(dp[i], 1 + dp[i - perfect])
        return dp[-1]
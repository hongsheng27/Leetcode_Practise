class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1, 1]
        if s[0] == '0': return 0
 
        for i in range(2, len(s) + 1):
            cur = 0
            if s[i - 1] != '0':
                cur += dp[1]
            if 10 <= int(s[i - 2:i]) <= 26:
                cur += dp[0]
            dp[0] = dp[1]
            dp[1] = cur
        return dp[-1]
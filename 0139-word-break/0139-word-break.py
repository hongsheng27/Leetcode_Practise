class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        print(wordSet)
        dp = [False for _ in range(len(s) + 1)]
        print(dp)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(len(s)):
                print(i, j, dp[j], s[j: i])
                if dp[j] and s[j: i] in wordSet:
                    dp[i] = True
        return dp[-1]
        

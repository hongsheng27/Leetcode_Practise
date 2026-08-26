class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxLen = max(map(len, wordDict))
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordSet = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - maxLen), i):
                if dp[j] and s[j: i] in wordSet: 
                    dp[i] = True
                    break
        return dp[-1]

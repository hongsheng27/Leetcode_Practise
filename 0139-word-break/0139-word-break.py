class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # dp[i] => if s[:i + 1] can be segmented to fit wordDict
        # dp[i] = dp[j] + (s[i - j] in wordDictSet)
        # tc: O(N ^ 2) sc: O(N + W)
        wordDictSet = set(wordDict)
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                res = dp[j] and (s[j: i] in wordDictSet)
                if res:
                    dp[i] = res
        print(dp)
        return dp[-1]
        # debug: 1.dp[i] = dp[j] + (s[j: i] in wordDictSet)
        # 2.for i in range(1, len(s)):
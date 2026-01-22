class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i, cache):
            if i >= len(s):
                return 1
            if i in cache: return cache[i]
            if s[i] == "0": return 0
            res = dfs(i + 1, cache)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2, cache)
            cache[i] = res
            return cache[i]
        return dfs(0, {})
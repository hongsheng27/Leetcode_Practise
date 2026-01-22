class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(remaining, cache):
            if not remaining:
                return 1
            if remaining in cache:
                return cache[remaining]
            if remaining[0] == "0":
                return 0
            # one digit
            res = dfs(remaining[1:], cache)
            # second digit
            if len(remaining) >= 2:
                two_digit = remaining[:2]
                if 10 <= int(two_digit) <= 26:
                    res += dfs(remaining[2:], cache)
            cache[remaining] = res
            return res
        
        return dfs(s, {})
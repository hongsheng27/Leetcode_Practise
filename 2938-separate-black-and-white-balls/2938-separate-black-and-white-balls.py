class Solution:
    def minimumSteps(self, s: str) -> int:
        res = amount1 = 0
        for c in s:
            if c == "1":
                amount1 += 1
            else:
                res += amount1
        return res
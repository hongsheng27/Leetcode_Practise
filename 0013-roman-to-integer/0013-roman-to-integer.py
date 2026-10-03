class Solution:
    def romanToInt(self, s: str) -> int:
        # while traversal
        # if correct order(big -> small), than add it
        # if wrong order, calculate it, add it, r += 1
        romanToNumber = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = r = 0
        while r < len(s):
            if r == len(s) - 1 or romanToNumber[s[r]] >= romanToNumber[s[r + 1]] :
                res += romanToNumber[s[r]]
            else:
                value = romanToNumber[s[r + 1]] - romanToNumber[s[r]]
                res += value
                r += 1
            r += 1
        return res
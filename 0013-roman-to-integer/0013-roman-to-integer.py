class Solution:
    def romanToInt(self, s: str) -> int:
        # make stack (I, 1)
        # if order is right, add number to stack
        # if stack[-1] and s[i + 1] order is reverse, pop and append it again
        # calculate in the end
        stack = []
        romanToNumber = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for c in s:
            if stack and stack[-1][1] < romanToNumber[c] and stack[-1][0] != "*":
                r, n = stack.pop()
                stack.append(("*", romanToNumber[c] - n))
            else:
                stack.append((c, romanToNumber[c]))
        res = 0
        for roman, number in stack:
            res += number
        return res
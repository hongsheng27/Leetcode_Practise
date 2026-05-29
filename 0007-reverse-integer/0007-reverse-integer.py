class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        def helper(x):
            if x == 0: return ""
            endDigit = x % 10
            res = x // 10
            resDigit = str(helper(res))
            return str(endDigit) + str(resDigit)
        reverseStr = helper(x)
        if reverseStr == "": return 0
        res = int(int(reverseStr))
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return sign * res
        
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            res = res * 10 + digit
        if res > 2 ** 31 - 1 or res < -(2 ** 31):
            return 0
        return res
        

        
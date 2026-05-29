class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2 ** 31)
        MAX = 2 ** 31 - 1
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            res = 10 * res + digit
            x = int(x / 10)
        
        if res < MIN or res > MAX: return 0
        return res

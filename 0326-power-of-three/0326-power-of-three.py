class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # n / 3 until abs = 1
        # -1 is exception
        # -2^31 <= n <= 2^31 - 1, around 10^ 9, but O(logn) should be fine
        # 07:00
        if n == -1: return False
        while abs(n // 3) >= 1:
            if n % 3:
                return False
            n = n // 3 
        return abs(n) == 1
        # 10: 36
     

        
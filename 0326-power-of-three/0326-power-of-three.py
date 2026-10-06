class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # n / 3 until abs = 1
        # -1 is exception
        # -2^31 <= n <= 2^31 - 1, around 10^ 9, but O(logn) should be fine
        # after dry run, n should be also multiple of 3
        if n < 0: return False
        while n > 1:
            if n % 3:
                return False
            n = n // 3 
        return n == 1
      
    
     

        
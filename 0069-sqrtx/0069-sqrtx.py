class Solution:
    def mySqrt(self, x: int) -> int:
        # do bs to x to find m
        # if x / m < m: r = m - 1
        # find less possible => ans 
        l = 1
        r = x
        res = 0
        while l <= r:
            m = (l + r) // 2
            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
 



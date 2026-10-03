class Solution:
    def mySqrt(self, x: int) -> int:
        # do bs to x to find m
        # if x / m < m: r = m - 1
        # find less possible => ans 
        #(Hign layer: 8:41)
        l = 1
        r = x
        res = 0
        while l <= r:
            m = (l + r) // 2
            if x / m >= m:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
        #(12:56) first try done



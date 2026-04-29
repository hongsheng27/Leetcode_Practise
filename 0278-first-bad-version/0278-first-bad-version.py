# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        res = r
        while l <= r:
            m = (l + r) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        return res
        
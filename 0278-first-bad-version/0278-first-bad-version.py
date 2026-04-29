# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m
        return l
        
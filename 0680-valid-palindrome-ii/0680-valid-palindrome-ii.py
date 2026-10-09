class Solution:
    def validPalindrome(self, s: str) -> bool:
        # solution1: two pointer, after miss match, do two pointer twice with left shift 1 and right shift 1, one of it success means True
        def helper(l, r):
            while l <= r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return helper(l + 1, r) or helper(l, r - 1)
        return True
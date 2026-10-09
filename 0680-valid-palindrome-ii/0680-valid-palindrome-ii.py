class Solution:
    def validPalindrome(self, s: str) -> bool:
        # solution1: two pointer, after miss match, do two pointer twice with left shift 1 and right shift 1, one of it success means True
        l = 0
        r = len(s) - 1
        def helper(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        while l < r:
            if s[l] != s[r]:
                return helper(l + 1, r) or helper(l, r - 1)
            l += 1
            r -= 1
        return True
        

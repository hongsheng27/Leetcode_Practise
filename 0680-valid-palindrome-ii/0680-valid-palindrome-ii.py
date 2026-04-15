class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                r -= 1
                l += 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return palindrome(l + 1, r) or palindrome(l, r - 1)
            l += 1
            r -= 1
        return True
        
        
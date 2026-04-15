class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(st):
            l = 0
            r = len(st) - 1
            while l < r:
                if st[l] != st[r]:
                    return False
                r -= 1
                l += 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return palindrome(s[l + 1: r + 1]) or palindrome(s[l: r])
            l += 1
            r -= 1
        return True
        
        
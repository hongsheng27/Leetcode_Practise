class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else: return False
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(l, r - 1) or isPalindrome(l + 1, r)
        return True
        
            
        
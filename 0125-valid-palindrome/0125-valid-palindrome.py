class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def isAlphaNumeric(self, c):
        return (ord("a") <= ord(c) <= ord("z") or
                ord("A") <= ord(c) <= ord("Z") or
                ord("0") <= ord(c) <= ord("9"))

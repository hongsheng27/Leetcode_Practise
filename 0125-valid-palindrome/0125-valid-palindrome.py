class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1       

        return True
    def isAlphaNumeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or 
                ord("0") <= ord(c) <= ord("9"))
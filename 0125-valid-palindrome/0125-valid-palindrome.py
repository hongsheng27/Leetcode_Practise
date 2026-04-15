class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(char):
            return (ord('a') <= ord(char) <= ord('z') or
                    ord('A') <= ord(char) <= ord('Z') or
                    ord('0') <= ord(char) <= ord('9'))

        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not isAlphanumeric(s[l]):
                l += 1
            while l < r and not isAlphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                print(l, r)
                return False
            l += 1
            r -= 1
        return True
            

       
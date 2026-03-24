class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        div = 1
        while x > div * 10:
            div *= 10
        while x:
            right = x % 10
            left = x // div

            if left != right: return False

            x = (x % div) // 10
            div /= 100
        return True
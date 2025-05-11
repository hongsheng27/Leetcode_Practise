class Solution(object):
    def isPalindrome(self, s):
        string = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        left, right = 0, len(string) - 1
        
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1       

        return True
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for shift in range(len(s)):
            ns = s[shift:] + s[:shift] 
            if goal == ns:
                return True
        return False
        
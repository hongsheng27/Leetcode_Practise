class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        s = s + s
        for i in range(len(s)):
            if s[i: i + n] == goal: return True
        return False
        
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        s = s + s
        time = 0
        for i in range(len(s)):
            if s[i: i + n] == goal: return True
            time += 1
            if time == n:
                break
        return False
        
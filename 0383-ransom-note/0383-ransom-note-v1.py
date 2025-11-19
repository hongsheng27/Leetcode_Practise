class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR, countM = [0] * 26, [0] * 26
        for c in ransomNote:
            countR[ord(c) - ord('a')] += 1
        for c in magazine:
            countM[ord(c) - ord('a')] += 1
        for i in range(26):
            if countR[i] > countM[i]: return False
        return True
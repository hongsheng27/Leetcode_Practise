class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR, countM = [0] * 26, [0] * 26
        for c in ransomNote:
            countR[ord(c) - ord('a')] += 1
        for c in magazine:
            countM[ord(c) - ord('a')] += 1
        for c in ransomNote:
            if countM[ord(c) - ord('a')] < countR[ord(c) - ord('a')]:
                return False
        return True
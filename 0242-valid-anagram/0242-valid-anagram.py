class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for c in s:
            countS[c] = countS.get(c, 0) + 1
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        return countS == countT
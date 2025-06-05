class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1Count =  [0] * 26
        s2Count = [0] * 26
        for i in s1:
            s1Count[ord(i) - ord('a')] += 1 
        for j in s2[:len(s1)]:
            s2Count[ord(j) - ord('a')] += 1 
        l = 0
        if s1Count == s2Count:
            return True
        for r in range(len(s1), len(s2)):
            s2Count[ord(s2[r]) - ord('a')] += 1
            s2Count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if s1Count == s2Count:
                return True
        return False

            
            
        
        
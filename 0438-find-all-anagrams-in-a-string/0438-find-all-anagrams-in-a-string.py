class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []

        count1, count2 = [0] * 26, [0] * 26
        
        for i in range(len(p)):
            count1[ord(p[i]) - ord('a')] += 1
            count2[ord(s[i]) - ord('a')] += 1
        
        res = []
        
        l = 0
        for r in range(len(p), len(s)):
            if count1 == count2: res.append(l)

            count2[ord(s[r]) - ord('a')] += 1
            count2[ord(s[l]) - ord('a')] -= 1

            l += 1

        if count1 == count2: res.append(l)
        return res

            


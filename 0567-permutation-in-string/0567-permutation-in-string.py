class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l, r = 0, len(s1) - 1
        s1_count = Counter(s1)
        count = {}
        for i in range(len(s1)):
            count[s2[i]] = 1 + count.get(s2[i], 0)

        while r < len(s2):
            if s1_count == count:
                return True
            count[s2[l]] -= 1
            if count[s2[l]] <= 0:
                del count[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                count[s2[r]] = 1 + count.get(s2[r], 0) 
        return False

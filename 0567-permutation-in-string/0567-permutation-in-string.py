class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_count = Counter(s1)
        count = defaultdict(int)
        for i in range(len(s1)):
            count[s2[i]] = 1 + count.get(s2[i], 0)

        if s1_count == count:
                return True
                
        for r in range(len(s1), len(s2)):
            count[s2[r]] += 1
            count[s2[r - len(s1)]] -= 1
            if count[s2[r - len(s1)]] == 0:
                del count[s2[r - len(s1)]]
            if count == s1_count:
                return True
        return False
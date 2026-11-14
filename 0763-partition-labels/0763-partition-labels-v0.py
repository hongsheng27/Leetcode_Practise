class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # make count
        # travese s, add s[r] into window count, count[s[r]] -= 1
        # make windowSet
        # once count[s[r]] == 0, clear += 1, len(clear) == len(window) means suceessful
       
        res = []
        count = Counter(s)
        window = set()
        l = clear = 0
        for r in range(len(s)):
            window.add(s[r])
            count[s[r]] -= 1
            
            if count[s[r]] == 0:
                clear += 1
            if clear == len(window):
                res.append(r - l + 1)
                clear = 0
                window = set()
                l = r + 1
        return res
            
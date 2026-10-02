class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # make new String, add elem on p1 and move, add elem on p2 and move util word1 or word2 go to the end, lastly, add reamining

        res = []
        p1 = p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            res.append(word1[p1])
            p1 += 1
            res.append(word2[p2])
            p2 += 1
        remaining = word1[p1:] or word2[p2:]
        for r in remaining:
            res.append(r)
        print(res)
        return "".join(res)

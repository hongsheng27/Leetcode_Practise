class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sortArr = sorted(set(arr))
        rankMap = {}
        for i in range(len(sortArr)):
            rankMap[sortArr[i]] = i + 1
        res = []
        for a in arr:
            res.append(rankMap[a])
        return res
        
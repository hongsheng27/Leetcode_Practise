class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # solution1: brute force - dfs, O(2^k) k might be 10 ^ 5 not work
        # how to know if the extreme learge number hidden in the deep?
        # 1.using heap? not work
        # 1 1 => 1
        # 1 2 6 => 6
        # 1 2 999 5 => 999
        #
        # 123
        # 165
        # find maximal 6 first? cost is 2 card? I think not work
        # 21:00
        # hint 1
        # anser property => total - minimal (N - k) subarray sum
        N = len(cardPoints)
        total = sum(cardPoints)
        value = 0
        for i in range(N - k):
            value += cardPoints[i]
        miniValue = value
        for r in range(N - k, N):
            l = r - (N - k)
            print(l, r)
            value += cardPoints[r]
            value -= cardPoints[l]
            miniValue = min(value, miniValue)
            print(miniValue)
        return total - miniValue
        # 38:00 debugging



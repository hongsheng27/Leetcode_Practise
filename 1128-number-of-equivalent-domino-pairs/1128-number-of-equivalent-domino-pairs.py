class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        # asssume only one pair
        freq = defaultdict(int)
        for first, second in dominoes:
            board = [0] * 10
            board[first] += 1
            board[second] += 1
            freq[tuple(board)] += 1
        res = 0
        for i in freq.values():
            if i > 1:
                res += (i * (i - 1) // 2)

        return res
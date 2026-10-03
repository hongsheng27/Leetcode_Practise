class Solution:
    def countCommas(self, n: int) -> int:
        # >= 10^ 3 number
        # >= 10 ^ 6 number(not consideration)
        # 02:45 finish high layer
        return max(0, n - 999)
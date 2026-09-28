class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        res = 0
        arr.sort()
        for num in arr:
            if num > res:
                res += 1
        return res


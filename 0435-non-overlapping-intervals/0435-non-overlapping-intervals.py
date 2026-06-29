class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        preEnd = float('-inf')
        res = 0
        for start, end in intervals:
            if start >= preEnd:
                preEnd = end
            else:
                res += 1
        return res

        
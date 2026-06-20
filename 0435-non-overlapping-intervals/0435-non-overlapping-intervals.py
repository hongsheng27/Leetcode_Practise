class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        preEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if preEnd <= start:
                preEnd = end
            else:
                res += 1
        return res

        
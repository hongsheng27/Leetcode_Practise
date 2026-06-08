class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        res = 0
        preEnd = intervals[0][1]

        for interval in intervals[1:]:
            if preEnd <= interval[0]:
                preEnd = interval[1]
            else:
                res += 1
                preEnd = min(preEnd, interval[1])
        return res

        
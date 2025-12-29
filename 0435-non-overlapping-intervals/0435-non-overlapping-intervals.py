class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        res = 0
        preEnd = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] < preEnd:
                if interval[1] < preEnd:
                    preEnd = interval[1]
                res += 1
            else:
                preEnd = interval[1]
        return res

        
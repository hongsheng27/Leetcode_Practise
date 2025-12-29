class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0

        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] < res[-1][1]:
                if interval[1] < res[-1][1]:
                    res[-1] = interval
            else:
                res.append(interval)
        return len(intervals) - len(res)

        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        last = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if start <= last[1]:
                last[1] = max(end, last[1])
            else:
                res.append(last)
                last = [start, end]
        res.append(last)
        return res

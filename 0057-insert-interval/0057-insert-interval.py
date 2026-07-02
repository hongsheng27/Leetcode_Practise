class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            # before newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)
            # after newInterval
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            # overlap
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        res.append(newInterval)
        return res
        
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        isInclude = False
        for i, interval in enumerate(intervals):
            start, end = interval
            # left
            if newInterval[0] > end:
                res.append([start, end])
            # right
            elif start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # middle 
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
            
       
        res.append(newInterval)
        return res
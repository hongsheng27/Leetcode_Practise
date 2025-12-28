class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                interval = res.pop()
                newInterval = [interval[0], max(interval[1], intervals[i][1])]
                res.append(newInterval)
            else:
                res.append(intervals[i])
        return res


        
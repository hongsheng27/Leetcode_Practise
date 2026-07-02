class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if end < newInterval[0]:
                res.append([start, end])
            elif start > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        res.append(newInterval)
        return res



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        merged = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]
            newStart, newEnd = merged
            if newStart > end:
                res.append([start, end])
            elif newEnd < start:
                return res + [merged] + intervals[i:]
            else:
                merged = [min(newStart, start), max(newEnd, end)]      
        res.append(merged)
        return res

        
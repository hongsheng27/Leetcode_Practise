class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        remove = 0
        valid = []
        for i in range(len(intervals)):
            if i > 0 and intervals[i][0] < valid[-1][1]:
                remove += 1
                continue
            valid.append(intervals[i])
        return remove
                

        
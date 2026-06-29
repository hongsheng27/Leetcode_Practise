class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        remove = 0
        preEnd = float('-inf')
        for i in range(len(intervals)):
            if i > 0 and intervals[i][0] < preEnd:
                remove += 1
                continue
            preEnd = intervals[i][1]
        return remove
                

        
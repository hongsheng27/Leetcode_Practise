class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < intervals[i - 1][1]:
                return False
        return True

        
        

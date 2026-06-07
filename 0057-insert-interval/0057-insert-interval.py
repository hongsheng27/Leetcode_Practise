class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        intervals.append(newInterval)
        intervals.sort()
        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                oldStart, oldEnd = stack.pop()
                end = max(oldEnd, interval[1])
                stack.append((oldStart, end))
            else:
                stack.append(interval)
        return stack

        
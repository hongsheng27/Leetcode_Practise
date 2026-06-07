class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                oldStart, oldEnd = stack.pop()
                stack.append([oldStart, max(oldEnd, interval[1])])
            else:
                stack.append(interval)
        return stack

        
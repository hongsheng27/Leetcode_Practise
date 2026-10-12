class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort
        # if overlap, keep the one end first, res += 1
        intervals.sort()
        stack = []
        res = 0
        for start, end in intervals:
            isAdd = True
            if stack and stack[-1][1] > start:
                stack[-1][1] = min(stack[-1][1], end)
                res += 1
            else: 
                stack.append([start, end])
        return res

        
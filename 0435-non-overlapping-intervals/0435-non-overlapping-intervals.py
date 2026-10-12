class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort
        # if overlap, keep the one end first, res += 1
        # 02:50
        intervals.sort()
        stack = []
        res = 0
        for start, end in intervals:
            isAdd = True
            if stack and stack[-1][1] > start:
                stack[-1][1] = min(stack[-1][1], end)
                isAdd = False
                res += 1
            if isAdd: stack.append([start, end])
        return res

        
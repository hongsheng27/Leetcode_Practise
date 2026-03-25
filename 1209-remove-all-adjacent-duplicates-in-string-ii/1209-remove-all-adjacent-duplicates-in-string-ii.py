class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        res = ""
        for s in stack:
            c, time = s
            res += c * time
        return res
        
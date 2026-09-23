class Solution:
    def minimumSteps(self, s: str) -> int:
        count = res = 0
        for c in s:
            if c == '1':
                count += 1
            if c == '0':
                res += count
        return res

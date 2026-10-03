class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        score = [0] * (n + 1)

        for t in trust:
            score[t[0]] -= 1
            score[t[1]] += 1
        for i in range(1, len(score)):
            if score[i] == n - 1:
                return i
        return -1
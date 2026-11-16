class Solution:
    def dietPlanPerformance(self, calories: list[int], k: int, lower: int, upper: int) -> int:
        res = 0
        def calScore(t):
            nonlocal res
            if t < lower:
                res -= 1
            elif t > upper:
                res += 1

        total = 0
        for i in range(k):
            total += calories[i]
        calScore(total)
        
        l = 0
        for r in range(k, len(calories)):
            total += calories[r]
            
            total -= calories[l]
            l += 1
                
            calScore(total)
        return res

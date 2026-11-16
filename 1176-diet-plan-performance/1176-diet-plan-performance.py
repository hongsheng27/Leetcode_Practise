class Solution:
    def dietPlanPerformance(self, calories: list[int], k: int, lower: int, upper: int) -> int:
        res = 0
        def scoreWindow(t):
            score = 0
            if t < lower:
                score -= 1
            elif t > upper:
                score += 1
            return score
            
        total = 0
        for i in range(k):
            total += calories[i]
        res += scoreWindow(total)
        
        l = 0
        for r in range(k, len(calories)):
            total += calories[r]
            
            total -= calories[l]
            l += 1
                
            res += scoreWindow(total)
        return res

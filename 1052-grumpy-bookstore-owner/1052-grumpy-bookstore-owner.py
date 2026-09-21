class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        base = 0
        extra = maxExtra = 0
        for i in range(len(customers)):
            if grumpy[i] == 0: 
                base += customers[i]
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]    
                maxExtra = max(maxExtra, extra)
        for r in range(minutes, len(customers)):
            l = r - minutes
            if grumpy[r] == 1:
                extra += customers[r]
            if grumpy[l] == 1:
                extra -= customers[l]
            maxExtra = max(maxExtra, extra)
        return base + maxExtra

class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)
        base = 0
        extra = 0

        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        maxExtra = extra

        for r in range(minutes, n):
            l = r - minutes + 1
            if grumpy[r] == 1:
                extra += customers[r]
            if grumpy[l - 1] == 1:
                extra -= customers[l - 1]
            maxExtra = max(maxExtra, extra)
        return base + maxExtra
            


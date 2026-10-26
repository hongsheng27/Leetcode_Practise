class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        # find fixed window with biggest total of grumpy[i] & customers[i]
        # keep moveing to find biggest total
        # return baseline(0) + biggest total(1 with special technical)
        l = baseline = max_gain = gain = 0
        
        for i in range(len(customers)):
            baseline += customers[i] if grumpy[i] == 0 else 0
        for i in range(minutes):
            gain += customers[i] if grumpy[i] == 1 else 0
        max_gain = gain
        for r in range(minutes, len(customers)):
            gain += customers[r] if grumpy[r] == 1 else 0
            gain -= customers[l] if grumpy[l] == 1 else 0
            l += 1
            max_gain = max(max_gain, gain)
        return baseline + max_gain


        
        
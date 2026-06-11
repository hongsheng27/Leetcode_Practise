class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        remaining = []
        for i in range(len(gas)):
            remaining.append(gas[i] - cost[i])

        total = 0
        minTotal = float('inf')
        minIndex = -1
        for i in range(len(remaining)):
            total += remaining[i]
            if total < minTotal:
                minTotal = total
                minIndex = i
        return minIndex + 1 if minIndex != len(gas) - 1 else 0
        
            


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        total = 0
        minTotal = float('inf')
        minIndex = -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < minTotal:
                minTotal = total
                minIndex = i
        return minIndex + 1 if minIndex != len(gas) - 1 else 0
        
            


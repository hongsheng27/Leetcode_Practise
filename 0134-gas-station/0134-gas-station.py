class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        res = 0
        currentTank = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            currentTank += diff

            if currentTank < 0:
                currentTank = 0
                res = i + 1
        return res

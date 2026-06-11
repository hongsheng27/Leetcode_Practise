class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        totalBalance = 0
        currentTank = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            currentTank += diff
            totalBalance += diff

            if currentTank < 0:
                currentTank = 0
                res = i + 1
        return res if totalBalance >= 0 else -1

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        tank = res = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                tank = 0
                res = i + 1
        return res
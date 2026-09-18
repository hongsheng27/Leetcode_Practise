class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)
        changeWindow = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                changeWindow += customers[i]
        l = 0
        maxChange = (0, minutes - 1, changeWindow) # (l, r, sum)
        for l in range(1, n - minutes + 1):
            r = l + minutes - 1
            if grumpy[r] == 1:
                changeWindow += customers[r]
            if grumpy[l - 1] == 1:
                changeWindow -= customers[l - 1]

            if changeWindow > maxChange[2]:
                maxChange = (l, r, changeWindow)

        for i in range(maxChange[0], maxChange[1] + 1):
            grumpy[i] = 0
        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
        return res
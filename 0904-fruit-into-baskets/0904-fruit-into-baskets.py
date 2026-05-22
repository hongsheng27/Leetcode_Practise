class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l = 0
        maxNum = 0
        for r in range(len(fruits)):
            while len(count) == 2 and fruits[r] not in count:
                maxNum = max(maxNum, r - l)
                count[fruits[l]] -= 1
                if not count[fruits[l]]: del count[fruits[l]]
                l += 1
            count[fruits[r]] = count.get(fruits[r], 0) + 1
        maxNum = max(maxNum, r - l + 1)
        return maxNum
        
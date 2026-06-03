class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = {}
        maxLen = 0
        for r in range(len(fruits)):
            fruit = fruits[r]
            count[fruit] = count.get(fruit, 0) + 1
            while len(count) > 2:
                maxLen = max(maxLen, r - l)
                count[fruits[l]] -= 1
                if not count[fruits[l]]: del count[fruits[l]]
                l += 1
        maxLen = max(maxLen, r - l + 1)
        return maxLen
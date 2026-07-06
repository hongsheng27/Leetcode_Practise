class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        l = res = 0
        for r in range(len(fruits)):
            window[fruits[r]] += 1
            while len(window) > 2:
                window[fruits[l]] -= 1
                if not window[fruits[l]]: del window[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
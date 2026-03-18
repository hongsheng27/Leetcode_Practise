class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l = res = 0 

        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            
            while len(count) == 3:
                count[fruits[l]] -= 1
                if not count[fruits[l]]:
                    del count[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res if res else r - l + 1


            

        
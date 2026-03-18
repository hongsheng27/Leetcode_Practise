class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l = res = 0 

        for r in range(len(fruits)):
            if fruits[r] not in count or not count[fruits[r]]:
                count[fruits[r]] = 1
            else:
                count[fruits[r]] += 1
            
            while len(count) == 3:
                count[fruits[l]] -= 1
                if not count[fruits[l]]:
                    del count[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res if res else r - l + 1


            

        
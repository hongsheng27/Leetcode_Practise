class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        have = l = res = 0 

        for r in range(len(fruits)):
            if fruits[r] not in count or not count[fruits[r]]:
                count[fruits[r]] = 1
                have += 1
            else:
                count[fruits[r]] += 1
            
            while have == 3:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    have -= 1  
                l += 1
            res = max(res, r - l + 1)
        return res if res else sum(count.values())


            

        
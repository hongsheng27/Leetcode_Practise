class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        middle = len(nums) // 2
        left, right = nums[:middle], nums[middle:]
        return self.sortList(self.sortArray(left), self.sortArray(right))

    def sortList(self, l1, l2):
        if not l1: return l2
        if not l2: return l1 
        res = []
        p1 = p2 = 0
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] <= l2[p2]:
                res.append(l1[p1])
                p1 += 1
            else:
                res.append(l2[p2])
                p2 += 1
        
        res += l1[p1:]
        res += l2[p2:]
        return res


        
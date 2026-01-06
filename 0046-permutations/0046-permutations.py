class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i >= len(nums):
                return [[]]
            nextPerm = []
            perm = backtrack(i + 1)

            for p in perm:
                for j in range(len(p)+1):
                    copyP = p.copy()
                    copyP.insert(j, nums[i])
                    nextPerm.append(copyP)
            return nextPerm
        return backtrack(0)


        
# This fails on Leetcode case, because the worst-case time complexity is O(n^2), although the average time complexity is O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        target_index = len(nums) - k
        def quicksort(l, r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if target_index < p:
                return quicksort(l, p - 1)
            elif target_index > p:
                return quicksort(p + 1, r)
            else:
                return nums[p]

        return quicksort(0, len(nums) - 1)



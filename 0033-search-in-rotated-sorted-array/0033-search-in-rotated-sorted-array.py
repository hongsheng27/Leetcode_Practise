class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    return m
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    return m

        return -1
            
        


        
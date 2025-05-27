class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        locate_side = 'right' if target <= nums[r] else 'left'

        res = [nums[-1], len(nums) - 1] # value, index
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                if nums[l] < res[0]:
                    res = [nums[l], l]
                break
            elif nums[l] <= nums[m]:
                l = m + 1
                print('1', l, r)
            else:
                if nums[m] < res[0]:
                    res = [nums[m], m]
                r = m - 1
                print('2', l, r)
        print(res)
        if locate_side == 'right':
            l, r = res[1], len(nums) - 1
        else:
            l, r = 0, res[1]

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1


            
        


        
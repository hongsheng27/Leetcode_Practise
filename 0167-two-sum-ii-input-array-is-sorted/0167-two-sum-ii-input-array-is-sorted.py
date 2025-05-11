class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 1, len(numbers)

        while left < right:
            if numbers[left - 1] + numbers[right - 1] < target:
                left += 1
            if numbers[left - 1] + numbers[right - 1] > target:
                right -= 1
            if numbers[left - 1] + numbers[right - 1] == target:
                return [left, right]
        
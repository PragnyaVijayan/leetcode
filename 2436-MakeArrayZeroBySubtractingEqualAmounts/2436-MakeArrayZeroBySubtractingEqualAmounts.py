# Last updated: 6/19/2025, 11:46:23 AM
class Solution(object):
    def minimumOperations(self, nums, count = 0):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all(num == 0 for num in nums):
            return count

        non_zero_nums = [num for num in nums if num > 0]

        if not non_zero_nums:
            return count

        x = min(non_zero_nums)
        nums = [num - x if num > 0 else 0 for num in nums]

        return self.minimumOperations(nums, count + 1)

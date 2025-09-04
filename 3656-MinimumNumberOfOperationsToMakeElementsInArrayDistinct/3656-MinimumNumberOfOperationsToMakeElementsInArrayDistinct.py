# Last updated: 9/4/2025, 1:28:07 AM
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        while len(set(nums)) < len(nums):
            #print('nums before: ', nums)
            nums = nums[3:]
            count += 1
            #print('nums after: ', nums)
            
        return count



        
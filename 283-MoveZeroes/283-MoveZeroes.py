# Last updated: 8/19/2025, 11:51:21 PM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        '''
        - can have multiple zeroes. have to create a new pointer for each
        '''

        write_index = 0  # pointer for the next non-zero

        # move non-zeros forward
        for read_index in range(len(nums)):
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                if read_index != write_index:
                    nums[read_index] = 0
                write_index += 1
        
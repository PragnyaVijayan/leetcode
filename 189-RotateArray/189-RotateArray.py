# Last updated: 8/22/2025, 11:34:18 PM
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        '''
        Modulus

        [1,2,3,4], k = 2 ;
            0 + 2 % 4 = 2
            1 + 2 % 4 = 3
            2 + 2 % 4 = 0
            3 + 2 % 4 = 1
        '''

        # len_nums = len(nums)

        # new_nums = [0] * len_nums

        # for num_index in range(0, len_nums):
        #     new_index = (num_index + k) % len_nums
        #     new_nums[new_index] = nums[num_index]
        #     #print('nums: ', nums)
        #     #print('new_nums: ', new_nums)

        # for i in range(len_nums):
        #     nums[i] = new_nums[i]
        # return nums

        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]

        
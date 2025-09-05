# Last updated: 9/5/2025, 3:29:08 PM
class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sum_of_window = []
        # i = 0
        
        # while i < len(nums):
        #     start = max(0, i - nums[i])
        #     #print(start, i)
        #     sum_of_window.append(sum(nums[start:i+1]))

        #     i += 1

        #     #print(sum_of_window)
        #     #print(i)
        
        # return sum(sum_of_window)

        prefix_sum = [0]
        sliding_sum = []

        total = 0

        for num in nums:
            total += num
            prefix_sum.append(total)
        
        #print('prefix sum: ', prefix_sum)

        for i in range(0, len(nums)):
            start = max(0, i - nums[i])
            sliding_sum.append(prefix_sum[i+1] - prefix_sum[start])
        
        #print('sliding window: ', sliding_sum)
        
        return sum(sliding_sum)

        




        
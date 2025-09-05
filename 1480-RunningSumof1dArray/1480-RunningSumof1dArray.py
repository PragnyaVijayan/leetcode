# Last updated: 9/5/2025, 12:07:43 AM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        running_sum = []
        running_sum.append(0)

        for num in nums:
            running_sum.append(num + running_sum[-1])
        
        del running_sum[0]
        
        return running_sum
        
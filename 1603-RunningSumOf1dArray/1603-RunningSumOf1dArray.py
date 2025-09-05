# Last updated: 9/5/2025, 3:29:22 PM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        running_sum = []
        total = 0

        for num in nums:
            total += num
            running_sum.append(total)
        
        return running_sum
        
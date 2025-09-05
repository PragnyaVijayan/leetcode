# Last updated: 9/5/2025, 12:32:27 AM
class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum_of_window = []
        i = 0
        
        while i < len(nums):
            start = max(0, i - nums[i])
            #print(start, i)
            sum_of_window.append(sum(nums[start:i+1]))

            i += 1

            #print(sum_of_window)
            #print(i)
        
        return sum(sum_of_window)



        
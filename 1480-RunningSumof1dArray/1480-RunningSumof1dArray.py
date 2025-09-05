# Last updated: 9/5/2025, 12:09:59 AM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total=0
        dummy=list(nums)
        for i,j in enumerate(nums):
           total=sum(nums[0:i+1])
           dummy[i]=total
           total=0
        return dummy

        
              
            
            
        
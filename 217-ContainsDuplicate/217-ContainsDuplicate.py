# Last updated: 8/22/2025, 11:34:17 PM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        return False
        
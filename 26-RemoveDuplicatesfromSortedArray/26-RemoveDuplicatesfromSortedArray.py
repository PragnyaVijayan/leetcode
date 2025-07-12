# Last updated: 7/11/2025, 6:23:23 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        '''
        - need to return number of unique elements in nums
        - edge case:
            - elements can repeat multiple times

        psuedocode:
        n = len(nums)
        i = 0
        #count_popped = 0

        while i < n:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                #count_popped += 1
            else:
                i += 1
        
        return len(nums)
        '''

        n = len(nums)
        i = 0
        #count_popped = 0

        while i < len(nums) - 1:
            # print(i)
            # print(nums)
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                #count_popped += 1
            else:
                i += 1
        
        return len(nums)
        
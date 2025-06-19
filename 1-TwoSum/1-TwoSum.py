# Last updated: 6/19/2025, 11:46:39 AM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        1) Do a nested for loop and add each and compare
        2) Can try sorting, but kinda inefficient. Number can be 9 and need to add 8 and 1 from both
        ends of the spectrum
        3) If you have a number1, you need to find value - number1 to find 
        number2. Number1 + number2 will be target
        
        '''

        # for i in range(0, len(nums) - 1):
        #     for j in range (i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             print([i, j])
        #             return([i, j])

        # return None

        nums_hash = set(nums)
        #print(nums_hash)

        for i in range(0, len(nums)):
            number1 = nums[i]
            number2 = target - number1
            print(number1, number2)
            if number2 in nums_hash and number1 in nums_hash:
                if nums.index(number2) != i:
                    return [i, nums.index(number2)]

        return None
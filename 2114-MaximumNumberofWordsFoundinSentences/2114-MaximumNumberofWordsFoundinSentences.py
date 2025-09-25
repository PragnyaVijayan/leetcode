# Last updated: 9/24/2025, 11:53:16 PM
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num
            num = str(num)
            for char in num:
                digit_sum += int(char)
        
        return abs(element_sum - digit_sum)
        
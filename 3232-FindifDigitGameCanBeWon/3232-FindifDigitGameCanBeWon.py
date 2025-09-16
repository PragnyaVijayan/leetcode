# Last updated: 9/15/2025, 11:50:32 PM
class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        sum_double_digits = 0
        sum_single_digits = 0

        for num in nums:
            if 1 <= num <= 9:
                sum_single_digits += num
            elif 10 <= num <= 99:
                sum_double_digits += num

        #print(sum_single_digits, sum_double_digits)
        return (sum_double_digits != sum_single_digits)

        
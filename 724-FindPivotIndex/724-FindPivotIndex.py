# Last updated: 9/5/2025, 3:29:28 PM
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_sum = [0]
        right_sum = [0]
        left_total = 0
        right_total = 0

        reverse_nums = nums[::-1]

        for i in range(0, len(nums)-1):
            left_total += nums[i]
            right_total += reverse_nums[i]

            left_sum.append(left_total)
            right_sum.append(right_total)
        
        right_sum = right_sum[::-1]

        # print(nums)
        # print(left_sum, right_sum)

        for i in range(0, len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
            
        return -1
        
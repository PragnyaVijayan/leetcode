# Last updated: 6/19/2025, 11:46:28 AM
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        #total_avg = sum(nums) / len(nums)
        average = float('-inf')
        l = 0
        sum_ = 0

        if len(nums) < k:
            return None

        if len(nums) == 1:
            return nums[0] / 1

        # while l <= (len(nums) - k):
        #     r = l + k 
        #     sum_ = 0

        #     for i in range(l, r):
        #         #print(nums[i])
        #         sum_ += nums[i]
            
        #     avg = sum_ / k
        #     average = max(average, avg)
        #     l += 1

        for i in range (0, k):
            sum_ += nums[i]
        
        average = max(average, (sum_/k))

        for i in range (k, len(nums)):
            previous = nums[i-k]
            next = nums[i]
            sum_ -= previous
            sum_ += next

            average = max(average, (sum_/k))

        return average

        
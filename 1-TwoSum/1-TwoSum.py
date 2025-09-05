# Last updated: 9/5/2025, 2:49:15 PM
class Solution(object):
    def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

#         # for i in range(0, len(nums)-1):
#         #     for j in range(i+1, len(nums)):
#         #         if nums[i] + nums[j] == target:
#         #             return [i,j]
                
#         # return None

#         nums_map = {}

#         for i, num in enumerate(nums):
#             if num not in nums_map:
#                 nums_map[num] = [i]
#             else:
#                 nums_map[num].append(i)


#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in nums_map:
#                 for j in nums_map[complement]:
#                     if i != j:
#                         return [i, j]
        
#         return None




        nums_map = {}  # num -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map:
                return [nums_map[complement], i]
            nums_map[num] = i

        return None

        
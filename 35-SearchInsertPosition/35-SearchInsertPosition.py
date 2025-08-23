# Last updated: 8/22/2025, 11:34:25 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        """
        Constraints:

        - sorted array
        - distinct integers

        - return target if found
        - else, return index where it would be found

        - O(log n)

        Brute force:
        - traverse an array. if num[i] == target, return n. O(n)
        - if num[i] != target and num[i+1] > target, return i+1

        Edge cases:
        - the list provided has 0, 1 elements


        """

        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            
            else:
                if i == 0 and nums[i] > target:
                    return i
                elif nums[i] != target:
                    if i + 1 < len(nums):
                        if nums[i + 1] > target and nums[i] < target:
                            return i + 1
                    elif i + 1 == len(nums):
                        return i + 1

        return None
        
# Last updated: 9/6/2025, 10:43:55 PM
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums_hash = {}
        for i in range(0, len(nums)):
            if nums[i] not in self.nums_hash:
                self.nums_hash[nums[i]] = [i]
            else:
                self.nums_hash[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random

        all_indexes = list(self.nums_hash[target])
        random_item = random.choice(all_indexes)
        return random_item

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
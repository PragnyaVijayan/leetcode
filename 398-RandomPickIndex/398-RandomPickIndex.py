# Last updated: 9/6/2025, 10:45:41 PM
class Solution(object):

    def __init__(self, nums):
        self.freq = defaultdict(list)
        self.nums = nums
        

    def pick(self, target):
        if target not in self.freq:
            for i in range(len(self.nums)):
                if self.nums[i] == target:
                    self.freq[target].append(i)

        return random.choice(self.freq[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# Last updated: 6/30/2025, 11:28:52 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []

        for i in range(0, len(nums)):
            print(nums[i])
            ans.append(nums[i])

        for i in range (len(nums), 2*len(nums)):
            print(nums[i - len(nums)])
            ans.append(nums[i - len(nums)])

        return ans
        
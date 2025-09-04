# Last updated: 9/4/2025, 1:28:36 AM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_range = 0
        while left <= right:
            #print('left: ', left)
            sum_range += self.nums[left]
            left += 1
            #print('sum_left: ', sum)
        
        #print('sum_total: ', sum)
        return sum_range
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
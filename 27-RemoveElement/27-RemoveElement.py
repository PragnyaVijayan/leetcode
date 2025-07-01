# Last updated: 6/30/2025, 11:14:42 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if val > 50:
            return len(nums)
        
        non_val_count = 0
        length_nums = len(nums)
        i = 0

        while i < length_nums:
            print(nums[i])
            if val != nums[i]:
                non_val_count += 1
                i += 1
            else:
                del nums[i]
                length_nums -= 1
                nums.append('_')

        
        print(non_val_count, nums)
        return (non_val_count)
        
# Last updated: 9/18/2025, 11:41:54 PM
class Solution(object):

    def getProduct(self, nums):
        result = 1
        for num in nums:
            result *= num
        
        return result
    
    def signFunc(self, x):
        if x > 0: 
            return 1
        elif x < 0:
            return -1
        else:
            return 0


    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.signFunc(self.getProduct(nums))


        
# Last updated: 9/5/2025, 12:00:21 AM
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        
        digit_sum = sum(int(d) for d in str(num))
        return self.addDigits(digit_sum)

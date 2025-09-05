# Last updated: 9/5/2025, 12:01:45 AM
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) == 1:
            return num
        
        digit_sum = sum(int(d) for d in str(num))
        return self.addDigits(digit_sum)

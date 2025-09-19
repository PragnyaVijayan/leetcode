# Last updated: 9/18/2025, 11:23:05 PM
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        digits = [int(digit) for digit in str(num)]
        #print(digits)

        count = 0
        for i in digits:
            if num % i == 0:
                count += 1

        return count
        
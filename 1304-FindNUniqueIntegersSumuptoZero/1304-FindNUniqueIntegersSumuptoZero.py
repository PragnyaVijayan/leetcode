# Last updated: 9/6/2025, 10:49:55 PM
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        sum_zero_arr = []

        count = 0
        num = 1
        while count <= n - 2:
            sum_zero_arr.append(num)
            sum_zero_arr.append(-num)
            count += 2
            num += 1
        
        if n % 2 == 1:
            sum_zero_arr.append(0)
        
        return sum_zero_arr


        
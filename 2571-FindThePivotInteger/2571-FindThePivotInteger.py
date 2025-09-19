# Last updated: 9/18/2025, 11:23:07 PM
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        1 2 3 4 5
        
        left_sum = 0, 1, 3, 6, 10
        right_sum = 0, 5, 9, 12, 14
        '''


        left_sum = [0]
        right_sum = [0]
        left_total = 0
        right_total = 0

        for i in range(1,n):
            left_total += i
            left_sum.append(left_total)
                
        for i in range(n, 1, -1):
            #print(i)
            right_total += i
            right_sum.append(right_total)
        
        right_sum = right_sum[::-1]
        #print(left_sum, right_sum)

        for i in range(0, n):
            if left_sum[i] == right_sum[i]:
                return i+1

        return -1
        
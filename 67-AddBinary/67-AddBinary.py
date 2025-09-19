# Last updated: 9/19/2025, 12:00:24 AM
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # Approach to get closest integer
        # i = 1
        # squared = []

        # while (i*i) <= x:
        #     squared.append(i*i)
        #     i += 1
        
        # i += 1
        # squared.append(i*i)

        # last_entry = squared[-1]
        # second_last = squared[-2]

        # if abs(last_entry - x) < abs(second_last - x):
        #     return squared.index(last_entry) + 1
        # else:
        #     return squared.index(second_last) + 1

        # Approach to get rounded down integer


        i = 1

        while (i*i) < x:
            i += 1
        
        if (i*i) == x:
            return i

        if (i*i) > x:
            return i - 1
        
        return i
        
        


        
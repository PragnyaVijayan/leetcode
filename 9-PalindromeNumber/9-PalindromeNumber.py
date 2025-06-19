# Last updated: 6/19/2025, 11:46:38 AM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        '''
            - Reverse string <-- O(n)
            - Have a for loop with iterator <-- O(n)
            - Check if same. If not, return False.

            Can make more optimized. O(n/2) using two-pointers
        '''

        # x = str(x)
        # x_reversed = "".join(reversed(x))

        # for i in range(0, len(x)):
        #     if x[i] != x_reversed[i]:
        #         return False
        # return True
        
        x = str(x)
        right = len(x) - 1
        left = 0

        while left < right:
            if x[right] != x[left]:
                return False
            
            right -= 1
            left += 1
        
        return True
        